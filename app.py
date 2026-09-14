import pandas as pd
import plotly.express as px
import streamlit as st


# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="Student Retention AI Agent",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# CUSTOM UI STYLE
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #f7f9fc;
    }

    /* Main content width */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Header */
    .hero {
        background: linear-gradient(135deg, #eef4ff, #ffffff);
        padding: 30px 35px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 38px;
        font-weight: 750;
        margin-bottom: 8px;
        color: #172033;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #5b6577;
        margin-bottom: 18px;
    }

    .status {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 20px;
        background: #ecfdf3;
        color: #16794c;
        font-size: 14px;
        font-weight: 600;
        border: 1px solid #cceedd;
    }

    /* Question area */
    .question-title {
        font-size: 22px;
        font-weight: 700;
        color: #172033;
        margin-bottom: 5px;
    }

    /* Understanding card */
    .understanding-card {
        background: white;
        padding: 20px 24px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 3px 12px rgba(20, 30, 50, 0.04);
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .understanding-title {
        font-size: 20px;
        font-weight: 700;
        color: #172033;
        margin-bottom: 15px;
    }

    /* Metric cards */
    .metric-card {
        background: #f8fafc;
        padding: 14px 16px;
        border-radius: 12px;
        border: 1px solid #e5eaf1;
        margin-bottom: 10px;
    }

    .metric-label {
        font-size: 12px;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .metric-value {
        font-size: 16px;
        font-weight: 650;
        color: #1f2937;
        margin-top: 3px;
    }

    /* Summary */
    .summary-card {
        background: white;
        padding: 22px 25px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 3px 12px rgba(20, 30, 50, 0.04);
        margin-top: 20px;
    }

    .summary-title {
        font-size: 20px;
        font-weight: 700;
        color: #172033;
        margin-bottom: 10px;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 46px;
        font-size: 16px;
        font-weight: 650;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #8a94a6;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e5eaf1;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    school_master = pd.read_csv(
        "final_cleaned_school_master.csv"
    )

    infrastructure = pd.read_csv(
        "final_cleaned_infrastructure.csv"
    )

    mid_day_meal = pd.read_csv(
        "final_cleaned_mid_day_meal.csv"
    )

    test_scores = pd.read_csv(
        "final_cleaned_test_scores.csv"
    )

    attendance = pd.read_csv(
        "final_cleaned_attendance.csv"
    )

    return (
        school_master,
        infrastructure,
        mid_day_meal,
        test_scores,
        attendance
    )


school_master, infrastructure, mid_day_meal, test_scores, attendance = load_data()


# ============================================================
# HERO HEADER
# ============================================================

st.markdown("""
<div class="hero">
<div class="hero-title">🎓 Student Retention & Welfare AI Agent</div>
<div class="hero-subtitle">Ask questions about education data in natural language and get automatic insights and visualizations.</div>
<div class="status">🟢 AI Agent Ready</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# QUESTION INPUT
# ============================================================

st.markdown(
    '<div class="question-title">💬 Ask your question</div>',
    unsafe_allow_html=True
)

question = st.text_input(
    "",
    placeholder="Example: Does electricity affect academic performance?",
    label_visibility="collapsed"
)

st.caption(
    "💡 Try: Compare test scores by electricity • "
    "Show highest attendance schools • "
    "How has attendance changed over time?"
)


# ============================================================
# QUESTION UNDERSTANDING
# ============================================================

def understand_question(question):

    q = question.lower().strip()

    # --------------------------------------------------------
    # WORD GROUPS
    # --------------------------------------------------------

    attendance_words = [
        "attendance",
        "attend",
        "present",
        "presence"
    ]

    score_words = [
        "test",
        "tests",
        "test score",
        "test scores",
        "score",
        "scores",
        "marks",
        "mark",
        "performance",
        "perform",
        "academic performance",
        "academic result",
        "results",
        "result"
    ]

    relationship_words = [
        "relationship",
        "relation",
        "correlation",
        "related",
        "affect",
        "impact",
        "connection",
        "associated"
    ]

    electricity_words = [
        "electricity",
        "electric",
        "power",
        "functional electricity",
        "electricity availability",
        "electricity access"
    ]

    compare_words = [
        "compare",
        "comparison",
        "difference",
        "versus",
        "vs",
        "between",
        "better",
        "higher",
        "lower",
        "affect",
        "impact",
        "effect"
    ]

    time_words = [
        "over time",
        "trend",
        "trends",
        "monthly",
        "daily",
        "day by day",
        "across dates",
        "changes over time",
        "changed over time"
    ]

    highest_words = [
        "highest",
        "top",
        "best",
        "maximum",
        "greatest",
        "leading",
        "strongest",
        "perform best"
    ]

    lowest_words = [
        "lowest",
        "worst",
        "bottom",
        "minimum",
        "poorest",
        "weakest",
        "perform worst"
    ]

    subject_words = [
        "subject",
        "subjects",
        "each subject",
        "by subject",
        "per subject"
    ]


    # ========================================================
    # 1. RELATIONSHIP
    # ========================================================

    if (
        any(word in q for word in attendance_words)
        and
        any(word in q for word in score_words)
        and
        any(word in q for word in relationship_words)
    ):

        return {
            "dataset": "relationship",
            "metric": "attendance rate and test score",
            "operation": "relationship",
            "group_by": "attendance vs test score",
            "chart": "scatter"
        }


    # ========================================================
    # 2. ELECTRICITY + TEST SCORES
    # ========================================================

    if (
        any(word in q for word in electricity_words)
        and
        any(word in q for word in score_words)
        and
        (
            any(word in q for word in compare_words)
            or
            ("with" in q and "without" in q)
        )
    ):

        return {
            "dataset": "test_scores",
            "metric": "average score percentage",
            "operation": "compare",
            "group_by": "functional electricity",
            "chart": "bar"
        }


    # ========================================================
    # 3. ATTENDANCE OVER TIME
    # ========================================================

    if (
        any(word in q for word in attendance_words)
        and
        any(word in q for word in time_words)
    ):

        return {
            "dataset": "attendance",
            "metric": "attendance_rate",
            "operation": "trend",
            "group_by": "date",
            "chart": "line"
        }


    # ========================================================
    # 4. TEST SCORES OVER TIME
    # ========================================================

    if (
        any(word in q for word in score_words)
        and
        any(word in q for word in time_words)
    ):

        return {
            "dataset": "test_scores",
            "metric": "score_percentage",
            "operation": "trend",
            "group_by": "date",
            "chart": "line"
        }


    # ========================================================
    # 5. HIGHEST ATTENDANCE
    # ========================================================

    if (
        any(word in q for word in attendance_words)
        and
        any(word in q for word in highest_words)
    ):

        return {
            "dataset": "attendance",
            "metric": "attendance_rate",
            "operation": "maximum",
            "group_by": "school_id",
            "chart": "bar"
        }


    # ========================================================
    # 6. LOWEST ATTENDANCE
    # ========================================================

    if (
        any(word in q for word in attendance_words)
        and
        any(word in q for word in lowest_words)
    ):

        return {
            "dataset": "attendance",
            "metric": "attendance_rate",
            "operation": "minimum",
            "group_by": "school_id",
            "chart": "bar"
        }


    # ========================================================
    # 7. TEST SCORES BY SUBJECT
    # ========================================================

    if (
        any(word in q for word in score_words)
        and
        any(word in q for word in subject_words)
    ):

        return {
            "dataset": "test_scores",
            "metric": "score_percentage",
            "operation": "average",
            "group_by": "subject",
            "chart": "bar"
        }


    # ========================================================
    # 8. GENERAL TEST SCORES
    # ========================================================

    if any(word in q for word in score_words):

        return {
            "dataset": "test_scores",
            "metric": "score_percentage",
            "operation": "average",
            "group_by": "school_id",
            "chart": "bar"
        }


    # ========================================================
    # 9. GENERAL ATTENDANCE
    # ========================================================

    if any(word in q for word in attendance_words):

        return {
            "dataset": "attendance",
            "metric": "attendance_rate",
            "operation": "average",
            "group_by": "school_id",
            "chart": "bar"
        }


    # ========================================================
    # 10. FALLBACK
    # ========================================================

    return {
        "dataset": "unknown",
        "metric": "unknown",
        "operation": "unknown",
        "group_by": "unknown",
        "chart": "bar"
    }


# ============================================================
# ASK AI
# ============================================================

if st.button("🤖 Ask AI"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        intent = understand_question(question)


        # ====================================================
        # WHAT AI UNDERSTOOD
        # ====================================================

        st.markdown("""
        <div class="understanding-card">

            <div class="understanding-title">
                🤖 What I understood
            </div>

        </div>
        """, unsafe_allow_html=True)


        col1, col2, col3 = st.columns(3)


        with col1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Dataset</div>
                    <div class="metric-value">{intent['dataset']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col2:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Analysis</div>
                    <div class="metric-value">{intent['operation']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col3:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Visualization</div>
                    <div class="metric-value">{intent['chart'].capitalize()}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # 1. RELATIONSHIP / SCATTER
        # ====================================================

        if intent["dataset"] == "relationship":

            attendance_avg = (
                attendance
                .groupby("school_id", as_index=False)
                ["attendance_rate"]
                .mean()
            )

            test_avg = (
                test_scores
                .groupby("school_id", as_index=False)
                ["score_percentage"]
                .mean()
            )

            result = pd.merge(
                attendance_avg,
                test_avg,
                on="school_id",
                how="inner"
            )

            fig = px.scatter(
                result,
                x="attendance_rate",
                y="score_percentage",
                hover_data=["school_id"],
                labels={
                    "attendance_rate": "Average Attendance Rate",
                    "score_percentage": "Average Test Score (%)"
                },
                title="Relationship Between Attendance and Test Scores"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            correlation = result[
                "attendance_rate"
            ].corr(
                result["score_percentage"]
            )

            st.markdown("""
            <div class="summary-card">
                <div class="summary-title">📝 AI Summary</div>
            """, unsafe_allow_html=True)

            st.write(
                f"The analysis compares attendance and test scores "
                f"across **{len(result)} schools**. "
                f"The correlation between the two variables is "
                f"**{correlation:.2f}**."
            )

            st.markdown("</div>", unsafe_allow_html=True)


        # ====================================================
        # 2. ATTENDANCE OVER TIME
        # ====================================================

        elif (
            intent["dataset"] == "attendance"
            and intent["operation"] == "trend"
        ):

            result = attendance.copy()

            result["date"] = pd.to_datetime(
                result["date"],
                errors="coerce"
            )

            trend = (
                result
                .groupby("date", as_index=False)
                ["attendance_rate"]
                .mean()
                .sort_values("date")
            )

            fig = px.line(
                trend,
                x="date",
                y="attendance_rate",
                labels={
                    "date": "Date",
                    "attendance_rate": "Average Attendance Rate"
                },
                title="Average Attendance Over Time"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            average_attendance = trend[
                "attendance_rate"
            ].mean()

            highest_day = trend.loc[
                trend["attendance_rate"].idxmax()
            ]

            lowest_day = trend.loc[
                trend["attendance_rate"].idxmin()
            ]

            st.markdown("""
            <div class="summary-card">
                <div class="summary-title">📝 AI Summary</div>
            """, unsafe_allow_html=True)

            st.write(
                f"The overall average attendance was "
                f"**{average_attendance:.2f}%**. "
                f"The highest average attendance was "
                f"**{highest_day['attendance_rate']:.2f}%**, "
                f"while the lowest was "
                f"**{lowest_day['attendance_rate']:.2f}%**."
            )

            st.markdown("</div>", unsafe_allow_html=True)


        # ====================================================
        # 3. TEST SCORES OVER TIME
        # ====================================================

        elif (
            intent["dataset"] == "test_scores"
            and intent["operation"] == "trend"
        ):

            result = test_scores.copy()

            if "date" in result.columns:

                result["date"] = pd.to_datetime(
                    result["date"],
                    errors="coerce"
                )

                trend = (
                    result
                    .groupby("date", as_index=False)
                    ["score_percentage"]
                    .mean()
                    .sort_values("date")
                )

                fig = px.line(
                    trend,
                    x="date",
                    y="score_percentage",
                    labels={
                        "date": "Date",
                        "score_percentage": "Average Test Score (%)"
                    },
                    title="Average Test Scores Over Time"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

                average_score = trend[
                    "score_percentage"
                ].mean()

                st.markdown("""
                <div class="summary-card">
                    <div class="summary-title">📝 AI Summary</div>
                """, unsafe_allow_html=True)

                st.write(
                    f"The overall average test score was "
                    f"**{average_score:.2f}%**."
                )

                st.markdown("</div>", unsafe_allow_html=True)

            else:

                st.warning(
                    "The test score dataset does not contain a date column."
                )


        # ====================================================
        # 4. TEST SCORES BY SUBJECT
        # ====================================================

        elif (
            intent["dataset"] == "test_scores"
            and intent["group_by"] == "subject"
        ):

            result = (
                test_scores
                .groupby("subject", as_index=False)
                ["score_percentage"]
                .mean()
                .sort_values(
                    "score_percentage",
                    ascending=False
                )
            )

            fig = px.bar(
                result,
                x="subject",
                y="score_percentage",
                labels={
                    "subject": "Subject",
                    "score_percentage": "Average Test Score (%)"
                },
                title="Average Test Scores by Subject"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            highest = result.iloc[0]

            lowest = result.iloc[-1]

            st.markdown("""
            <div class="summary-card">
                <div class="summary-title">📝 AI Summary</div>
            """, unsafe_allow_html=True)

            st.write(
                f"**{highest['subject']}** has the highest average "
                f"test score at **{highest['score_percentage']:.2f}%**, "
                f"while **{lowest['subject']}** has the lowest at "
                f"**{lowest['score_percentage']:.2f}%**."
            )

            st.markdown("</div>", unsafe_allow_html=True)


        # ====================================================
        # 5. ELECTRICITY + TEST SCORES
        # ====================================================

        elif (
            intent["dataset"] == "test_scores"
            and intent["group_by"] == "functional electricity"
        ):

            scores = test_scores.copy()

            infra = infrastructure.copy()

            scores["school_id_clean"] = (
                scores["school_id"]
                .astype(str)
                .str.strip()
            )

            infra["school_id_clean"] = (
                infra["school_id"]
                .astype(str)
                .str.strip()
            )

            result = pd.merge(
                scores,
                infra[
                    [
                        "school_id_clean",
                        "has_electricity"
                    ]
                ],
                on="school_id_clean",
                how="inner"
            )


            def electricity_status(value):

                value = str(value).strip().lower()

                if value in [
                    "yes",
                    "y",
                    "1",
                    "true",
                    "hai"
                ]:

                    return "With functional electricity"

                elif value in [
                    "no",
                    "n",
                    "0",
                    "false",
                    "nahi",
                    "nahin"
                ]:

                    return "Without functional electricity"

                else:

                    return "Unknown"


            result["electricity_status"] = (
                result["has_electricity"]
                .apply(electricity_status)
            )

            result = result[
                result["electricity_status"] != "Unknown"
            ]

            comparison = (
                result
                .groupby("electricity_status", as_index=False)
                ["score_percentage"]
                .mean()
            )

            fig = px.bar(
                comparison,
                x="electricity_status",
                y="score_percentage",
                labels={
                    "electricity_status": "Electricity Status",
                    "score_percentage": "Average Test Score (%)"
                },
                title="Average Test Scores by Functional Electricity"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


            with_electricity = comparison.loc[
                comparison["electricity_status"]
                == "With functional electricity",
                "score_percentage"
            ]

            without_electricity = comparison.loc[
                comparison["electricity_status"]
                == "Without functional electricity",
                "score_percentage"
            ]


            if (
                len(with_electricity) > 0
                and len(without_electricity) > 0
            ):

                with_score = with_electricity.iloc[0]

                without_score = without_electricity.iloc[0]

                difference = with_score - without_score


                if difference > 0:

                    better_group = (
                        "schools with functional electricity"
                    )

                elif difference < 0:

                    better_group = (
                        "schools without functional electricity"
                    )

                else:

                    better_group = (
                        "both groups have the same average score"
                    )


                st.markdown("""
                <div class="summary-card">
                    <div class="summary-title">📝 AI Summary</div>
                """, unsafe_allow_html=True)

                st.write(
                    f"Schools with functional electricity have an "
                    f"average test score of **{with_score:.2f}%**, "
                    f"while schools without functional electricity "
                    f"have an average score of **{without_score:.2f}%**. "
                    f"The difference is approximately "
                    f"**{abs(difference):.2f} percentage points**. "
                    f"Overall, {better_group}."
                )

                st.markdown("</div>", unsafe_allow_html=True)


            else:

                st.warning(
                    "Could not find both electricity groups in the data."
                )


        # ====================================================
        # 6. HIGHEST ATTENDANCE
        # ====================================================

        elif (
            intent["dataset"] == "attendance"
            and intent["operation"] == "maximum"
        ):

            result = (
                attendance
                .groupby("school_id", as_index=False)
                ["attendance_rate"]
                .mean()
                .sort_values(
                    "attendance_rate",
                    ascending=False
                )
                .head(10)
            )

            fig = px.bar(
                result,
                x="school_id",
                y="attendance_rate",
                labels={
                    "school_id": "School",
                    "attendance_rate": "Average Attendance Rate (%)"
                },
                title="Schools with Highest Average Attendance"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            highest = result.iloc[0]

            st.markdown("""
            <div class="summary-card">
                <div class="summary-title">📝 AI Summary</div>
            """, unsafe_allow_html=True)

            st.write(
                f"**{highest['school_id']}** has the highest "
                f"average attendance at "
                f"**{highest['attendance_rate']:.2f}%**."
            )

            st.markdown("</div>", unsafe_allow_html=True)


        # ====================================================
        # 7. LOWEST ATTENDANCE
        # ====================================================

        elif (
            intent["dataset"] == "attendance"
            and intent["operation"] == "minimum"
        ):

            result = (
                attendance
                .groupby("school_id", as_index=False)
                ["attendance_rate"]
                .mean()
                .sort_values(
                    "attendance_rate",
                    ascending=True
                )
                .head(10)
            )

            fig = px.bar(
                result,
                x="school_id",
                y="attendance_rate",
                labels={
                    "school_id": "School",
                    "attendance_rate": "Average Attendance Rate (%)"
                },
                title="Schools with Lowest Average Attendance"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            lowest = result.iloc[0]

            st.markdown("""
            <div class="summary-card">
                <div class="summary-title">📝 AI Summary</div>
            """, unsafe_allow_html=True)

            st.write(
                f"**{lowest['school_id']}** has the lowest "
                f"average attendance at "
                f"**{lowest['attendance_rate']:.2f}%**."
            )

            st.markdown("</div>", unsafe_allow_html=True)


        # ====================================================
        # 8. GENERAL TEST SCORES
        # ====================================================

        elif intent["dataset"] == "test_scores":

            result = (
                test_scores
                .groupby("school_id", as_index=False)
                ["score_percentage"]
                .mean()
                .sort_values(
                    "score_percentage",
                    ascending=False
                )
                .head(10)
            )

            fig = px.bar(
                result,
                x="school_id",
                y="score_percentage",
                labels={
                    "school_id": "School",
                    "score_percentage": "Average Test Score (%)"
                },
                title="Average Test Scores by School"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            highest = result.iloc[0]

            st.markdown("""
            <div class="summary-card">
                <div class="summary-title">📝 AI Summary</div>
            """, unsafe_allow_html=True)

            st.write(
                f"**{highest['school_id']}** has the highest "
                f"average test score among the schools shown, "
                f"at **{highest['score_percentage']:.2f}%**."
            )

            st.markdown("</div>", unsafe_allow_html=True)


        # ====================================================
        # 9. GENERAL ATTENDANCE
        # ====================================================

        elif intent["dataset"] == "attendance":

            result = (
                attendance
                .groupby("school_id", as_index=False)
                ["attendance_rate"]
                .mean()
                .sort_values(
                    "attendance_rate",
                    ascending=False
                )
                .head(10)
            )

            fig = px.bar(
                result,
                x="school_id",
                y="attendance_rate",
                labels={
                    "school_id": "School",
                    "attendance_rate": "Average Attendance Rate (%)"
                },
                title="Average Attendance by School"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            overall_average = (
                attendance["attendance_rate"].mean()
            )

            st.markdown("""
            <div class="summary-card">
                <div class="summary-title">📝 AI Summary</div>
            """, unsafe_allow_html=True)

            st.write(
                f"The overall average attendance across the "
                f"dataset is **{overall_average:.2f}%**. "
                f"The chart shows the top 10 schools based on "
                f"their average attendance."
            )

            st.markdown("</div>", unsafe_allow_html=True)


        # ====================================================
        # 10. FALLBACK
        # ====================================================

        else:

            st.warning(
                "I could not understand that question yet. "
                "Try asking about attendance, test scores, "
                "subjects, electricity, or relationships."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    🎓 Student Retention & Welfare AI Agent
    &nbsp; • &nbsp;
    Natural-language education data analysis
</div>
""", unsafe_allow_html=True)