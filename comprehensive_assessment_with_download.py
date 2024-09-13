import streamlit as st
import pandas as pd

# عنوان التطبيق
st.title("Comprehensive Personality Assessment")

# مقدمة التقييم
st.write("""
### Welcome to the Personality Assessment!
This test will cover multiple areas: Emotional Development, Social Development, and Cognitive Development.
Each area has 5 questions. At the end, you will see a matrix of your answers.
""")

# الأقسام الرئيسية
st.write("## Emotional Development")

# التطور العاطفي - 5 أسئلة
emotional_q1 = st.radio("1. How do you usually feel when someone interrupts you during a task?", 
                        ('Frustrated', 'Annoyed', 'Indifferent', 'Don’t know'))
emotional_q2 = st.radio("2. When you feel sad, what do you do?", 
                        ('Talk to a friend', 'Keep it to yourself', 'Express it creatively', 'Not sure'))
emotional_q3 = st.radio("3. How do you react when someone compliments you?", 
                        ('Feel embarrassed', 'Feel proud', 'Doubt their sincerity', 'Say thank you'))
emotional_q4 = st.radio("4. How do you deal with stress?", 
                        ('Take a break', 'Keep working', 'Talk to someone', 'Ignore it'))
emotional_q5 = st.radio("5. When you’re angry, how do you usually calm down?", 
                        ('Take deep breaths', 'Talk it out', 'Shut down', 'Other'))

st.write("## Social Development")

# التطور الاجتماعي - 5 أسئلة
social_q1 = st.radio("1. How do you approach new people in social settings?", 
                     ('Confidently', 'Cautiously', 'Avoid them', 'Other'))
social_q2 = st.radio("2. How do you handle group disagreements?", 
                     ('Try to mediate', 'Take a side', 'Stay quiet', 'Leave the group'))
social_q3 = st.radio("3. When someone needs help, how do you respond?", 
                     ('Offer help immediately', 'Wait for them to ask', 'Ignore them', 'Offer help hesitantly'))
social_q4 = st.radio("4. How do you feel about working in teams?", 
                     ('Enjoy it', 'Dislike it', 'Depends on the team', 'Feel neutral'))
social_q5 = st.radio("5. How do you respond to social invitations?", 
                     ('Excited', 'Reluctant', 'Decline often', 'Depends on the event'))

st.write("## Cognitive Development")

# التطور المعرفي - 5 أسئلة
cognitive_q1 = st.radio("1. How do you approach problem-solving?", 
                        ('Logically', 'Creatively', 'With hesitation', 'Ask for help'))
cognitive_q2 = st.radio("2. How do you process new information?", 
                        ('Analyze it deeply', 'Take it at face value', 'Doubt it', 'Forget it quickly'))
cognitive_q3 = st.radio("3. How do you handle complex tasks?", 
                        ('Break it into steps', 'Tackle it all at once', 'Feel overwhelmed', 'Delegate it'))
cognitive_q4 = st.radio("4. How do you make decisions?", 
                        ('Quickly', 'After careful thought', 'With uncertainty', 'Seek advice first'))
cognitive_q5 = st.radio("5. How do you feel about learning new things?", 
                        ('Excited', 'Indifferent', 'Nervous', 'Not sure'))

# إنشاء مصفوفة للإجابات
answers = {
    'Emotional Development': [emotional_q1, emotional_q2, emotional_q3, emotional_q4, emotional_q5],
    'Social Development': [social_q1, social_q2, social_q3, social_q4, social_q5],
    'Cognitive Development': [cognitive_q1, cognitive_q2, cognitive_q3, cognitive_q4, cognitive_q5]
}

# تحويل المصفوفة إلى DataFrame
df = pd.DataFrame(answers, index=[1, 2, 3, 4, 5])

# عرض مصفوفة الإجابات
st.write("## Your Answers Matrix:")
st.dataframe(df)

# خيار لتنزيل الإجابات في ملف CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download your answers as CSV", data=csv, file_name='personality_assessment_answers.csv', mime='text/csv')
