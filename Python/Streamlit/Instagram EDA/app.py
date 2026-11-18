import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Instagram EDA", page_icon="📊", layout="wide")
sns.set_style("whitegrid")


# ---------- Load & clean (same steps as the notebook) ----------
@st.cache_data
def load_data():
    raw = pd.read_csv("Instagram_Analytics.csv")
    df = raw.copy()

    df.drop(columns=["post_id", "account_id"], inplace=True)

    num_col = df.select_dtypes(include=["int", "float"]).columns
    for col in num_col:
        df[col] = df[col].fillna(df[col].mean())

    df["post_datetime"] = pd.to_datetime(df["post_datetime"], dayfirst=True, errors="coerce")
    df["post_date"] = pd.to_datetime(df["post_date"], dayfirst=True, errors="coerce")

    # Outliers -> replaced with median (IQR method)
    for col in num_col:
        Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        mask = (df[col] < lower) | (df[col] > upper)
        df.loc[mask, col] = df[col].median()

    return raw, df


raw_df, df = load_data()
num_col = df.select_dtypes(include=["int", "float"]).columns.tolist()

# ---------- Sidebar filters ----------
st.sidebar.header("Filters")

media = st.sidebar.multiselect(
    "Media type", sorted(df["media_type"].unique()), default=sorted(df["media_type"].unique())
)
category = st.sidebar.multiselect(
    "Content category", sorted(df["content_category"].unique()), default=sorted(df["content_category"].unique())
)
source = st.sidebar.multiselect(
    "Traffic source", sorted(df["traffic_source"].unique()), default=sorted(df["traffic_source"].unique())
)

fdf = df[
    df["media_type"].isin(media)
    & df["content_category"].isin(category)
    & df["traffic_source"].isin(source)
]

st.title("📊 Instagram Post Performance & Engagement - EDA")
st.caption("Goal: find out how Instagram posts perform and what type of content people like the most")

if fdf.empty:
    st.warning("No data for the selected filters. Please change the filters in the sidebar.")
    st.stop()

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["Overview", "Charts", "Data"])

# ===== Overview =====
with tab1:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Posts", f"{len(fdf):,}")
    c2.metric("Avg Likes", f"{fdf['likes'].mean():,.0f}")
    c3.metric("Avg Engagement Rate", f"{fdf['engagement_rate'].mean():.4f}")
    c4.metric("Avg Reach", f"{fdf['reach'].mean():,.0f}")

    st.subheader("Dataset info")
    rows, cols = raw_df.shape
    st.write(f"Original data: **{rows:,} rows** and **{cols} columns**")

    left, right = st.columns(2)
    with left:
        st.write("Statistical summary (filtered data)")
        st.dataframe(fdf[num_col].describe())
    with right:
        st.write("Null values in original data")
        st.dataframe(raw_df.isnull().sum().rename("null_count"))
        st.write(f"Duplicate rows (after dropping IDs): **{raw_df.drop(columns=['post_id', 'account_id']).duplicated().sum()}**")

# ===== Charts =====
with tab2:
    # Correlation heatmap
    st.subheader("Correlation Between Numerical Variables")
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.heatmap(fdf[num_col].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribution of Likes")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(data=fdf, x="likes", bins=50, ax=ax)
        ax.set_xlabel("Number of Likes")
        ax.set_ylabel("Number of Posts")
        st.pyplot(fig)

    with col2:
        st.subheader("Number of Posts by Media Type")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.countplot(data=fdf, x="media_type", ax=ax)
        ax.set_xlabel("Media Type")
        ax.set_ylabel("Number of Posts")
        st.pyplot(fig)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Average Likes by Media Type")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(data=fdf, x="media_type", y="likes", errorbar=None, ax=ax)
        ax.set_xlabel("Media Type")
        ax.set_ylabel("Average Likes")
        st.pyplot(fig)

    with col4:
        st.subheader("Number of Posts by Traffic Source")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.countplot(data=fdf, x="traffic_source", ax=ax)
        ax.set_xlabel("Traffic Source")
        ax.set_ylabel("Number of Posts")
        plt.setp(ax.get_xticklabels(), rotation=30)
        st.pyplot(fig)

    st.subheader("Average Engagement Rate by Content Category")
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.barplot(data=fdf, x="content_category", y="engagement_rate", errorbar=None, ax=ax)
    ax.set_xlabel("Content Category")
    ax.set_ylabel("Average Engagement Rate")
    plt.setp(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Reach vs Impressions")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(data=fdf.sample(min(3000, len(fdf)), random_state=1), x="reach", y="impressions", ax=ax)
        ax.set_xlabel("Reach")
        ax.set_ylabel("Impressions")
        st.pyplot(fig)
        st.caption("Showing a random sample of up to 3,000 points so the chart loads fast.")

    with col6:
        st.subheader("Average Engagement Rate by Posting Hour")
        hourly = fdf.groupby("post_hour")["engagement_rate"].mean()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.lineplot(x=hourly.index, y=hourly.values, marker="o", ax=ax)
        ax.set_xlabel("Posting Hour (24-Hour Format)")
        ax.set_ylabel("Average Engagement Rate")
        ax.set_xticks(range(0, 24, 2))
        st.pyplot(fig)

# ===== Data =====
with tab3:
    st.subheader("Cleaned data (filtered)")
    st.dataframe(fdf.head(100))
    st.download_button(
        "Download filtered data as CSV",
        fdf.to_csv(index=False).encode("utf-8"),
        file_name="instagram_filtered.csv",
        mime="text/csv",
    )
