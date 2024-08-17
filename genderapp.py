import streamlit as st
import pickle

model = pickle.load(open('gender.pkl', 'rb'), encoding='latin1')

def run():
    st.title("Gender Classification using Machine Learning")
    
    ## Long Hair
    hair_display = ('No','Yes')
    hair_options = list(range(len(hair_display)))
    hair_models = st.selectbox("Person has a Long Hair ",hair_options, format_func=lambda x: hair_display[x])

  ## Forehead Height
    fh= st.slider('Enter Forehead Height')

    ## Forehead Width
    fw= st.slider('Enter Forehead Width')

    ## Nose Wide
    nose_wide = ('No','Yes')
    nose_wide_options = list(range(len(nose_wide)))
    nose_models_wide = st.selectbox("Person has a Wide Nose ",nose_wide_options, format_func=lambda x: nose_wide[x])

    ## Nose Long
    nose_long = ('No','Yes')
    nose_long_options = list(range(len(nose_long)))
    nose_models_long = st.selectbox("Person has a Long Nose",nose_long_options, format_func=lambda x: nose_long[x])

    ## Thin Lips
    lips = ('No','Yes')
    lips_options = list(range(len(lips)))
    lips_model = st.selectbox("Person has a Thin Lips", lips_options, format_func=lambda x: lips[x])


    ## Distance Nose
    dnose = ('No','Yes')
    dnose_options = list(range(len(dnose)))
    dnose_model = st.selectbox("Person has long distance between Nose and Lips",dnose_options, format_func=lambda x: dnose[x])



    if st.button("Submit"):
        features = [[hair_models, fh, fw, nose_models_wide, nose_models_long,lips_model,dnose_model]]
        print(features)
        prediction = model.predict(features)
        weight = [str(i) for i in prediction]
        ans = ', '.join(weight)
        if ans==0:
            st.error("Error in the Inputs: Please Try Again")

        else:
            st.success("The Person's Gender is:"+" "+ans)


            

run()