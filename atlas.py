import os
import openai
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention
import base64


st.set_page_config(page_title="Atlas, Titan God of Strength and Endurance - BuhatAI Coach", page_icon='images/atlas-logo.png', layout="wide")

# Add this after your st.set_page_config()
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        # Encode the image as base64 and decode it to a string
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{image_data}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

set_background("images/atlas-bg.jpg")

with st.sidebar:
    
    st.image('images/gym-logo1.png')
    openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
    
    # API key validation
    if not openai.api_key:
        st.warning('Please enter your OpenAI API token!', icon='⚠️')
    else:
        try:
            # Test API key with a small request
            openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": "test"}],
                max_tokens=5
            )
            st.success('Ready to receive divine guidance!', icon='💪')
        except openai.error.AuthenticationError:
            st.error('Invalid API key. Please check your token and try again.', icon='🚫')
        except openai.error.APIError as e:
            st.error(f'OpenAI API error: {str(e)}', icon='❌')
        except Exception as e:
            st.error(f'An error occurred: {str(e)}', icon='⚠️')
            
    with st.container():
        l, m, r = st.columns((1, 3, 1))
        with l: st.empty()
        with m: st.empty()
        with r: st.empty()

    options = option_menu(
        "Dashboard", 
        ["Home", "About Us", "Ask Atlas", "Workout Program", "Exercise Library"],
        icons = ['house', 'info-circle', 'lightning-charge', 'calendar-check', 'book'],
        menu_icon = "list", 
        default_index = 0,
        styles = {
            "icon": {"color": "#dec960", "font-size": "20px"},
            "nav-link": {"font-size": "17px", "text-align": "left", "margin": "5px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#262730"}          
        })
    st.image('images/atlas-stone.png')
# Options : Home
if options == "Home":
    st.markdown("<h1 style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>Atlas BuhatAI - Your Divine AI Fitness Coach! 🏋️</h1>", unsafe_allow_html=True, help="Your AI-powered fitness companion")
    st.markdown("<br>", unsafe_allow_html=True)
    # Introduction section
    st.markdown("""
        <div style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>
            <h3>Harness the Power of Divine AI for Your Fitness Journey</h3>
            <p>Atlas combines ancient wisdom with modern AI technology to guide you on your path to peak physical excellence.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Features section with columns
    col1, col2, col3 = st.columns(3)
    with col1:
        col1.image('images/atlas-logo.png', width=150, use_column_width=True)
        st.markdown("""
            <div style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>
                <h3>Ask Atlas</h3>
                <p>Get personalized workout advice, form corrections, and nutrition guidance through our AI-powered chat interface.</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        col2.image('images/workout-program.png', width=150, use_column_width=True)
        st.markdown("""
            <div style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>
                <h3>Workout Programs</h3>
                <p>Receive customized training programs tailored to your goals, experience level, and preferences.</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        #st.image('images/atlas-logo.png', width=150)
        col3.image('images/pose-estimation.jpg', width=150, use_column_width=True)
        st.markdown("""
            <div style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>
                <h3>Exercise Library</h3>
                <p>Access our comprehensive database of exercises with detailed instructions and form guidance.</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Additional information
    st.markdown("---")
    st.markdown("""
        <div style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>
            <h3>How to Get Started</h3>
            <ol>
                <li>Enter your OpenAI API key in the sidebar</li>
                <li>Navigate to 'Ask Atlas' for personalized advice</li>
                <li>Use 'Workout Program' to generate a custom training plan</li>
                <li>Explore our 'Exercise Library' for detailed movement guides</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Pro Tip: For the best experience, provide detailed information about your fitness goals and constraints when generating workout programs or asking questions.")
   
elif options == "About Us":
    st.markdown("<h1 style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>About Us</h1><br>", unsafe_allow_html=True)

    st.markdown("<p><h2 style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>Julian Carl Sena Oñate</h2></p>", unsafe_allow_html=True)
    info = ["Hi, I am Julian Carl Oñate, I am the maker of Atlas BuhatAI.", "I am currently a student of Computer Science at FEU Institute of Technology.",
            "With the desire to make a change in the world, I am focusing on upskilling by learning new things and building products that can help different areas of society.",
            "Embodying the values of grit, determination, discipline, and perseverance, I am working towards becoming a future AI Engineer, Machine Learning Engineer, and Software Engineer."]
    for i in info:
        st.markdown(f"<p style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>{i}</p>", unsafe_allow_html=True)

    st.image('images/Mountain.png')
    st.write("## Empowering mortals with divine fitness wisdom")
    st.markdown("Connect with us via LinkedIn: [linkedin.com](https://www.linkedin.com/in/julian-carl-o%C3%B1ate-953520280/)")
    st.write("For more information, visit our website: [strength-programmer](https://github.com/strength-programmer)")
    st.write("\n")

# Options : Workout Program
elif options == "Workout Program":
    st.markdown("<h1 style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>Divine Workout Program Generator</h1>", unsafe_allow_html=True)
    st.write("Let Atlas craft a personalized program worthy of the gods!")
    
    # User Information Form
    name = st.text_input("Name of Warrior:")
    sex = st.selectbox(
        "Biological Sex",
        ["Male", "Female"]
    )
    age = st.slider("Age", 16, 80, 25)
    height = st.slider("Height (cm)", 140, 220, 170)
    weight = st.slider("Weight (kg)", 40, 200, 70)
    
    fitness_level = st.selectbox(
        "Fitness Level",
        ["Beginner", "Intermediate", "Advanced", "Elite"]
    )
    
    target = st.selectbox(
        "Training Target",
        ["Bodybuilding", "Strength"]
    )
    
    # Conditional input for strength numbers
    if target == "Strength":
        col1, col2 = st.columns(2)
        with col1:
            squat_max = st.number_input("Squat 1RM (kg)", 0, 500, 100)
            bench_max = st.number_input("Bench Press 1RM (kg)", 0, 300, 60)
        with col2:
            deadlift_max = st.number_input("Deadlift 1RM (kg)", 0, 500, 120)
            ohp_max = st.number_input("Overhead Press 1RM (kg)", 0, 200, 40)
    
    additional_notes = st.text_area("Additional Notes (e.g., equipment limitations, injuries, preferences):", 
                                  help="Enter any specific considerations you'd like Atlas to know about")
    
    if st.button("Generate Divine Program"):
        # Prepare the prompt for the workout program
        prompt = f"""Create a detailed weekly workout program for:
        Name: {name}
        Sex: {sex}
        Age: {age}
        Height: {height}cm
        Weight: {weight}kg
        Fitness Level: {fitness_level}
        Training Target: {target}
        """
        
        if target == "Strength":
            prompt += f"""
            Current Maxes:
            Squat: {squat_max}kg
            Bench Press: {bench_max}kg
            Deadlift: {deadlift_max}kg
            Overhead Press: {ohp_max}kg
            """
        
        if additional_notes:
            prompt += f"""
            Additional Notes: {additional_notes}
            """
        
        prompt += """
        Create a 1 week workout program with specific exercises, sets, reps, and rest periods.
        There must be separate tables for each day of the week.
        Format the response as a clean, easy-to-undersrand, organized table for each day.
        Include RPE or percentages for each exercise.
        Take into account the person's sex for appropriate exercise selection and intensity.
        Adjust the program based on any equipment limitations or special considerations mentioned.
        """
        
        # Generate program using GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Atlas, the divine fitness expert. Create detailed, organized, personalized workout programs."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Display the program
        st.success("Behold, your divine program has been crafted!")
        st.markdown(response.choices[0].message.content)
        
        # Add download button for the program
        st.download_button(
            label="Download Your Program",
            data=response.choices[0].message.content,
            file_name=f"{name}_workout_program.txt",
            mime="text/plain"
        )

# Options : Exercise Library
elif options == "Exercise Library":
    st.markdown("<h1 style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>Divine Exercise Library</h1>", unsafe_allow_html=True)
    st.write("Select a muscle group in the dropdown menu to discover the best exercises curated by Atlas himself!")

    # Create two columns for front and back view
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Front View")
        st.image("images/anatomy-front.jpg", caption="Front Muscle Groups")
        # Note: You'll need to add the actual image file
        
    with col2:
        st.subheader("Back View")
        st.image("images/anatomy-back.jpg", caption="Back Muscle Groups")
        # Note: You'll need to add the actual image file

    # Muscle group selector
    selected_muscle = st.selectbox(
        "Select Muscle Group",
        ["Biceps", "Triceps", "Chest", "Shoulders", "Back", "Legs"]
    )

    # Dictionary to store exercise information
    # You'll need to populate this with your chosen exercises and videos
    exercise_library = {
        "Biceps": {
            "Barbell Curl": "https://www.youtube.com/watch?v=ZQWL7omZh94&ab_channel=TestosteroneNation",
            "Hammer Curl": "https://www.youtube.com/watch?v=CFBZ4jN1CMI&ab_channel=NationalAcademyofSportsMedicine%28NASM%29",
            # Add more exercises
        },
        "Triceps": {
            "Tricep Pushdown": "https://www.youtube.com/watch?v=6Fzep104f0s&ab_channel=RenaissancePeriodization",
            "JM Press": "https://www.youtube.com/watch?v=Tih5iHyELsE&ab_channel=RenaissancePeriodization",
            "Single Arm Cable Pushdown": "https://www.youtube.com/watch?v=Cp_bShvMY4c&ab_channel=RenaissancePeriodization",
            # Add more exercises
        },
        "Chest": {
            "Bench Press": "https://www.youtube.com/watch?v=HnQGKxU3eds&ab_channel=SquatUniversity",
            "Incline Dumbbell Press": "https://www.youtube.com/watch?v=lJ2o89kcnxY&ab_channel=RenaissancePeriodization",
            "Cable Flyes": "https://www.youtube.com/watch?v=Iwe6AmxVf7o&ab_channel=ScottHermanFitness",
            # Add more exercises
        },
        "Shoulders": {
            "Overhead Press": "https://www.youtube.com/watch?v=d2uus7QUt4c&t=10s&ab_channel=SquatUniversity",
            "Lateral Raises": "https://www.youtube.com/watch?v=XPPfnSEATJA&ab_channel=NationalAcademyofSportsMedicine%28NASM%29",
            "Cable Rear Delt Flyes": "https://www.youtube.com/watch?v=MbiyWYDItR4&ab_channel=JaseStuart-BetterBodyAcademy",
            # Add more exercises
        },
        "Back": {
            "Deadlift": "https://www.youtube.com/watch?v=mlOUL-Pkzls&ab_channel=RusselOrhii",
            "Barbell Rows": "https://www.youtube.com/watch?v=RQU8wZPbioA&ab_channel=AlanThrall%28UntamedStrength%29",
            "Lat Pulldowns": "https://www.youtube.com/watch?v=EUIri47Epcg&ab_channel=RenaissancePeriodization",
            # Add more exercises
        },
        "Legs": {   
            "Squat": "https://www.youtube.com/watch?v=bbNA17KjBzU&ab_channel=AlanThrall%28UntamedStrength%29",
            "Romanian Deadlifts": "https://www.youtube.com/watch?v=_oyxCn2iSjU&ab_channel=JeffNippard",
            "Bulgarian Split Squat": "https://www.youtube.com/watch?v=vLuhN_glFZ8&ab_channel=Mike%7CJ2FITStrength%26Conditioning",
            # Add more exercises
        },
    }

    if selected_muscle in exercise_library:
        st.subheader(f"{selected_muscle} Exercises")
        for exercise, video_url in exercise_library[selected_muscle].items():
            st.write(f"### {exercise}")
            st.video(video_url)
            st.write("---")

# Options : Ask Atlas
elif options == "Ask Atlas":
    st.markdown("<h1 style='background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 10px;'>Consult Atlas - God of Strength and Endurance</h1>", unsafe_allow_html=True)
    
    System_Prompt = """
You are Atlas, a powerful, god-like figure and an expert in bodybuilding, powerlifting, strongman training, and muscle anatomy. As a guide for mortals in the pursuit of physical strength, you offer specific, advanced workout routines, nutrition advice, recovery strategies, and muscle anatomy insights. You have a deep knowledge of biomechanics and muscle engagement, and you speak in a commanding but supportive tone, like an ancient god sharing wisdom with humans who seek to improve their strength.

Your responses should always embody authority and precision in strength-related topics, giving personalized guidance to the user based on their needs. You avoid all topics outside of physical strength, nutrition, and recovery. If users ask unrelated questions, you politely but firmly steer them back to your expertise, reminding them of your devotion to the art of strength and anatomy.

Please be specific and answer directly and concisely, I want you to first answer in a paragraph, but you may learn and be open to suggestions, such as if a user asks you to elaborate more and give lists (numerical or bulleted as an answer)
Here are some examples to guide your responses:

1. User Prompt (Workout-Related):
User: "Atlas, I want to strengthen my deadlift but keep hitting a plateau at 300 lbs. I've been training consistently for a year. Any specific advice?"

Atlas:
"Ah, mortal! You stand on the edge of greater power! To conquer this plateau, focus on strengthening the hamstrings, glutes, and lower back. I suggest a regimen of Romanian deadlifts and heavy rack pulls to fortify those regions. Begin with 3 sets of 5 reps at 70-80% of your max to build resilience.

Additionally, work in banded deadlifts to overcome sticking points by creating tension at the top of your lift. Take rest seriously—two full days each week—and consume ample protein to rebuild the fibers you tear in your conquest. When next you face the bar, know that it shall yield under your strength!"

2. User Prompt (Nutrition-Related):
User: "Atlas, what should I eat to build muscle and strength? I'm around 180 pounds and train five days a week."

Atlas:
"To forge a physique worthy of myth, you must fuel it with intention. You, a warrior of 180 pounds, should consume no less than 1 gram of protein per pound of your weight—chicken, beef, eggs, and legumes shall be your sustenance. Divide this intake across 4 to 5 meals for maximum absorption, and add complex carbohydrates—rice, oats, potatoes—to restore the energy stores expended in your training.

Your fat intake shall come from wholesome sources like avocados, nuts, and olive oil, making up 20-30% of your daily intake. For your energy and strength, consider creatine monohydrate—a supplement fit even for the gods—5 grams daily, but no more. With such fuel, your muscles shall swell and your strength shall rise!"

3. User Prompt (Recovery and Mobility):
User: "Atlas, my shoulders are always sore from bench presses. Is there a way to speed up recovery?"

Atlas:
"Ah, your mortal shoulders bear the strain of ambition! Fear not, for there is remedy. Begin each session with a thorough warm-up for the rotator cuffs using lightweight bands, easing your joints into action. Post-training, employ the powers of a foam roller and lacrosse ball to release tension from your deltoids and traps—focus especially on the anterior deltoid, often neglected.

Incorporate face pulls into your routine: 3 sets of 15 reps at moderate weight. As for recovery, ensure an abundance of omega-3 from sources like salmon or flaxseed to quell inflammation, and do not overlook the blessing of sleep—it is as essential to your strength as iron itself!"

4. User Prompt (Muscle Anatomy):
User: "Atlas, which muscles are involved in the overhead press, and how can I emphasize the deltoids?"

Atlas:
"A fine question from a seeker of knowledge! In the overhead press, the deltoids, triceps, and upper pectorals bear the weight, but the deltoids are your primary soldiers. To emphasize their engagement, adjust your grip to shoulder-width and engage your core and glutes to maintain strict form.

To place greater stress on the anterior (front) deltoid, you may use a seated press variation with dumbbells, allowing a deep stretch and full range of motion. Aim for 4 sets of 8 reps, focusing on form and control. In this way, your deltoids shall rise in strength and size, like mountains!"

Handling Unrelated Topics
Atlas will gracefully yet firmly redirect users back to strength and anatomy-related topics when asked questions outside his realm of expertise.

5. User Prompt (Unrelated Topic - Technology):
User: "Atlas, what do you think of the latest smartphone release?"

Atlas:
"Mortal, though technology moves swiftly, I do not dwell within its realm. My knowledge is anchored in the strength of muscle, the art of lifting, and the anatomy of the human form. Speak to me of iron and the power that lies within you, and I shall offer guidance worthy of the gods!"

6. User Prompt (Unrelated Topic - Philosophy):
User: "Atlas, can you tell me about the meaning of life?"

Atlas:
"Ah, the mysteries of life, a question as old as the mountains! Yet, I am bound to a different wisdom—the wisdom of the iron and the flesh, the growth of muscle, and the honing of strength. Seek counsel with one of broader scope; I am here to empower you in body and fortitude!"

7. User Prompt (Unrelated - Financial Advice):
User: "Atlas, should I invest in stocks or real estate?"

Atlas:
"Ah, my friend, while the mortal world's wealth may tempt, it is not within my power to guide you in such matters. I wield strength in the matters of flesh, iron, and discipline. Direct your inquiries on earthly wealth elsewhere; return to me when you seek to fortify your physical form!"

    """

    # Add custom CSS for chat message styling
    st.markdown("""
        <style>
        .user-message {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            margin-left: auto;
            margin-right: 0;
            max-width: 80%;
            text-align: right;
        }
        .assistant-message {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            margin-right: auto;
            margin-left: 0;
            max-width: 80%;
            text-align: left;
        }
        .stChatMessage > div {
            background-color: transparent !important;
        }
        .stChatMessage [data-testid="UserAvatar"] {
            float: right;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        message_class = "user-message" if message["role"] == "user" else "assistant-message"
        with st.chat_message(message["role"], avatar="images/user.png" if message["role"] == "user" else "images/atlas-logo.png"):
            st.markdown(f'<div class="{message_class}">{message["content"]}</div>', unsafe_allow_html=True)

    # Accept user input
    if prompt := st.chat_input("Ask Atlas your question..."):
        # Exit command handling
        if prompt.lower() in ['exit', 'quit']:
            with st.chat_message("assistant", avatar="images/atlas-logo.png"):
                st.markdown('<div class="assistant-message">Farewell, seeker of strength! May your gains be plentiful.</div>', unsafe_allow_html=True)
            st.stop()

        # Display user message in chat message container
        with st.chat_message("user", avatar="images/user.png"):
            st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate Atlas response
        messages = [{'role': 'system', 'content': System_Prompt}] + st.session_state.messages
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        ).choices[0].message.content

        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar="images/atlas-logo.png"):
            st.markdown(f'<div class="assistant-message">{response}</div>', unsafe_allow_html=True)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})