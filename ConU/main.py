import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Intro to ConUGPT",
    page_icon="👋",
    layout='wide',
    initial_sidebar_state="expanded"
)


st.title('Welcome to our ConUGPT!')
st.markdown('''
A customized GPT that helps students find information about their Concorida teachers.
With this app, you can easily find out which professors are teaching a particular course,
and even learn about the ratings of individual teachers.
This app is perfect for students who want to stay informed about their teachers and make informed decisions about their education.
With its intuitive interface and powerful search capabilities, you will shine this semester! ''')
st.divider()
st.markdown('### :thinking_face: Have you ever thought...')
st.markdown("")
col1, col2, col3 = st.columns(3, gap='medium')
with col1:
    st.write("I wish I can see the corresponding teachers of each class...I have to go all the way to the enrollment page to see the instructures :(")
    st.image("ConU/img/search.jpg")
   
with col2:
    st.write("I want to know who is the best teacher of the class. ")
    st.image("ConU/img/survey.jpg")
    
with col3:
    st.write("It's very annoying to search every single teacher, making tons of tabs!")
    st.image("ConU/img/stress.jpg")
st.divider()


st.markdown("### :thumbsup: We are here to help you!")

st.markdown("#### :question: How does it work?")
st.write("We used OpenAI API playground and GPT store to create the chatbox. Then, we feed the data of Concordia. Voila! Here is the expert of Concordia!")

st.markdown("#### :question:  What kind of questions can I ask?")
st.write("Below are the examples of the commands:")

with st.chat_message("user"):
    st.write("Who are the teachers of comp 233? Who has the best rate among them?")
with st.chat_message("ai"):
    st.write("John Doe, Charlie Walsh, and Logan Hart are teaching comp 233. John Doe has the best rate of 4.3.")
st.markdown("")

with st.chat_message("user"):
    st.write("What are some classes taught by John Doe?")
with st.chat_message("ai"):
    st.write("John Doe teaches comp 233 and comp 248 this semester. ")
st.markdown("")

with st.chat_message("user"):
    st.write("What is the name of the class with code 'comp 335'?")
with st.chat_message("ai"):
    st.write(" 'Introduction to Theoretical Computer Science' is the name of the class.")
st.markdown("")

st.write("You can also ask general info about the school.")
with st.chat_message("user"):
    st.write("When was Concordia founded?")
with st.chat_message("ai"):
    st.write("Concordia University was founded on August 24, 1974.")
st.markdown("")
st.markdown("#### :exclamation: Increase the accuracy")
st.info('''Change your prompt in case you suspect you did not get a complete response
            Example: write "who are the teachers for soen 287?"
                    instead of "who teaches soen 287?"
''')
st.info('Please try removing the white space after the command.')
st.markdown("")



html_string = '''
<!DCTYPE html>
<html style="height: 100%;">
<head>
<title>ConUGPT</title>
<style>
        body {
            height: 100%;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
    </style>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
        <script type="text/javascript">
        (function(d, t) {
            var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
            v.onload = function() {
                window.voiceflow.chat.load({
                    verify: { projectID: '65ac744084bfc6caadf6d527' },
                    url: 'https://general-runtime.voiceflow.com',
                    versionID: 'production'
                });
            }
            v.src = "https://cdn.voiceflow.com/widget/bundle.mjs"; v.type = "text/javascript"; s.parentNode.insertBefore(v, s);
        })(document, 'script');
    </script>
</head>
<body>
    <div>
        <h1 style="font-family: sans-serif">Ask Here!</h1>
    </div>
    <span style='font-size:50px;'>&#8595;</span>

</body>
</html>
'''

with st.sidebar:
    components.html(html_string, height=705)

st.header(":arrow_left: Now open the sidebar to start!")
st.text("You can always adjust the size of the sidebar")

st.markdown("")
st.markdown("")
st.markdown("")
with st.expander("Image credit"):
    st.write('"https://www.freepik.com/free-vector/student-stress-concept-illustration_27828937.htm#query=busy&position=25&from_view=search&track=sph&uuid=a92733f7-98da-4176-b339-1dc45a007a0d"')
    st.write('"https://www.freepik.com/free-vector/customer-survey-concept-illustration_5841882.htm#from_view=detail_author"')
    st.write('"https://www.freepik.com/free-vector/search-concept-illustration_4957155.htm#page=3&position=2&from_view=author&uuid=bf2feb3f-fb5a-417f-b3e1-cc9452fb97ac"')
    st.write('Images by storyset on Freepik')

# st.link_button("Click here to try ConUGPT!", "https://conugpt.netlify.app/", type='primary')
