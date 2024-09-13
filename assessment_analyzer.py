import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# قراءة ملف CSV
st.title("Personality Assessment Analyzer based on MCAF")

uploaded_file = st.file_uploader("Upload the CSV file", type="csv")

if uploaded_file is not None:
    # قراءة البيانات من ملف CSV
    df = pd.read_csv(uploaded_file)

    st.write("### Raw Data:")
    st.dataframe(df)

    # تحليل النتائج بناءً على MCAF لكل مجال
    emotional_scores = {"Frustrated": 3, "Annoyed": 2, "Indifferent": 1, "Don’t know": 0,
                        "Talk to a friend": 3, "Keep it to yourself": 2, "Express it creatively": 3, "Not sure": 1,
                        "Feel embarrassed": 1, "Feel proud": 3, "Doubt their sincerity": 2, "Say thank you": 3,
                        "Take a break": 3, "Keep working": 2, "Talk to someone": 3, "Ignore it": 1,
                        "Take deep breaths": 3, "Talk it out": 2, "Shut down": 1, "Other": 0}

    social_scores = {"Confidently": 3, "Cautiously": 2, "Avoid them": 1, "Other": 0,
                     "Try to mediate": 3, "Take a side": 2, "Stay quiet": 1, "Leave the group": 0,
                     "Offer help immediately": 3, "Wait for them to ask": 2, "Ignore them": 1, "Offer help hesitantly": 1,
                     "Enjoy it": 3, "Dislike it": 1, "Depends on the team": 2, "Feel neutral": 1,
                     "Excited": 3, "Reluctant": 2, "Decline often": 1, "Depends on the event": 1}

    cognitive_scores = {"Logically": 3, "Creatively": 3, "With hesitation": 1, "Ask for help": 2,
                        "Analyze it deeply": 3, "Take it at face value": 1, "Doubt it": 2, "Forget it quickly": 0,
                        "Break it into steps": 3, "Tackle it all at once": 2, "Feel overwhelmed": 1, "Delegate it": 1,
                        "Quickly": 2, "After careful thought": 3, "With uncertainty": 1, "Seek advice first": 2,
                        "Excited": 3, "Indifferent": 1, "Nervous": 1, "Not sure": 0}

    # تحويل الإجابات إلى درجات
    df['Emotional Score'] = df['Emotional Development'].map(emotional_scores)
    df['Social Score'] = df['Social Development'].map(social_scores)
    df['Cognitive Score'] = df['Cognitive Development'].map(cognitive_scores)

    # حساب المجموع لكل مجال
    total_emotional = df['Emotional Score'].sum()
    total_social = df['Social Score'].sum()
    total_cognitive = df['Cognitive Score'].sum()

    # عرض النتائج
    st.write("### Results Summary:")
    st.write(f"Total Emotional Score: {total_emotional}/15")
    st.write(f"Total Social Score: {total_social}/15")
    st.write(f"Total Cognitive Score: {total_cognitive}/15")

    # إنشاء تصورات بيانية للنتائج
    st.write("### Visualizations:")
    scores = {'Emotional': total_emotional, 'Social': total_social, 'Cognitive': total_cognitive}
    categories = list(scores.keys())
    values = list(scores.values())

    fig, ax = plt.subplots()
    ax.bar(categories, values, color=['lightblue', 'lightgreen', 'lightcoral'])
    ax.set_ylim(0, 15)
    ax.set_ylabel('Score')
    ax.set_title('Overall Scores by Category')

    st.pyplot(fig)

    # رسم التصور البياني بالتفصيل لكل مجال
    st.write("### Detailed Score Distribution")

    # تصورات تفصيلية لكل مجال
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    sns.barplot(x=categories, y=values, ax=axes[0], palette="Blues")
    sns.barplot(x=categories, y=values, ax=axes[1], palette="Greens")
    sns.barplot(x=categories, y=values, ax=axes[2], palette="Reds")

    axes[0].set_title('Emotional Development')
    axes[1].set_title('Social Development')
    axes[2].set_title('Cognitive Development')

    st.pyplot(fig)

    # إضافة تحليل نصي مفصل مع توصيات بناءً على الدرجات
    st.write("### Full Report:")
    
    if total_emotional > 12:
        st.success("Your emotional development is excellent. Keep up the good work!")
    elif total_emotional > 8:
        st.warning("You have good emotional development, but there's room for improvement.")
    else:
        st.error("You might want to work on improving emotional management and awareness.")

    if total_social > 12:
        st.success("Your social development is very strong. You have excellent social skills!")
    elif total_social > 8:
        st.warning("Your social skills are good, but there's room to grow.")
    else:
        st.error("Consider focusing more on teamwork, communication, and social interactions.")

    if total_cognitive > 12:
        st.success("Your cognitive skills are top-notch! You're great at problem-solving and learning.")
    elif total_cognitive > 8:
        st.warning("Your cognitive development is solid, but you can still enhance your critical thinking and problem-solving skills.")
    else:
        st.error("Work on improving how you approach learning, problem-solving, and decision-making.")

    # زر لتنزيل التقرير
    report = f"""
    Personality Assessment Report
    =============================
    Emotional Development Score: {total_emotional}/15
    Social Development Score: {total_social}/15
    Cognitive Development Score: {total_cognitive}/15

    Recommendations:
    - Emotional Development: {"Excellent" if total_emotional > 12 else "Good with room for improvement" if total_emotional > 8 else "Needs improvement"}
    - Social Development: {"Excellent" if total_social > 12 else "Good with room for improvement" if total_social > 8 else "Needs improvement"}
    - Cognitive Development: {"Excellent" if total_cognitive > 12 else "Good with room for improvement" if total_cognitive > 8 else "Needs improvement"}
    """
    st.download_button("Download Full Report", data=report, file_name="personality_assessment_report.txt")
