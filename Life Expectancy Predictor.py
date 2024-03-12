import streamlit as st

## Banner

# Display the banner image
st.image('https://www.who.int/ResourcePackages/WHO/assets/dist/images/logos/en/h-logo-blue.svg', use_column_width=True)


## UI
st.title('World Health Organisation Life Expectancy Calculator')


## Function
def predictLifeExpectancy():
    question = st.radio('Do you consent to using advanced population data, which may include protected information, for better accuracy?', ('Yes', 'No'))

    if question == 'Yes':
        st.write('This model requires 11 inputs, please hit "enter" when you have entered your inputs:')

        infant = st.number_input('Please enter your value for "Infant Deaths": ', step=1.0)
        under_5 = st.number_input('Please enter your value for "Under 5 Deaths": ', step=1.0)
        adult = st.number_input('Please enter your value for "Adult Mortality": ', step=1.0)
        hep_b = st.number_input('Please enter your value for "Hepatitis_B": ', step=1.0)
        bmi = st.number_input('Please enter your value for "BMI": ')
        GDP = st.number_input('Please enter your value for "GDP per Capita": ')

#        region = st.text_input("Please enter your region: ").lower()
# Trying dropbox for regions
        location = st.selectbox('What\'s you region?',
                                ('Central America and Caribbean', 'European Union', 'North America', 'Rest of Europe', 'South America')
                                )
        
        cent_am = 0
        eu = 0
        na = 0
        rest_eu = 0
        sa = 0

# Dropbox ifs


        if location == 'Central America and Caribbean':
            cent_am = 1
        elif location == 'European Union':
            eu = 1
        elif location == 'North America':
            na = 1
        elif location == 'Rest of Europe':
            rest_eu = 1
        elif location == 'South America':
            sa = 1
            

#        if region == 'european union':
#            eu = 1
#        elif region == 'south america':
#            sa = 1
#        elif region == 'central america and caribbean':
#            cent_am = 1
#        elif region == 'rest of europe':
#            rest_eu = 1
#        elif region == 'north america':
#            na = 1

        m0 = 84.1045
        m1 = -0.0695
        m2 = -0.0490
        m3 = -0.0444
        m4 = -0.0059
        m5 = -0.1250
        m6 = 4.567e-05
        m7 = 1.7790
        m8 = 1.3544
        m9 = 1.8501
        m10 = 0.06751
        m11 = 1.5910

        y = m0 + m1 * infant + m2 * under_5 + m3 * adult + m4 * hep_b + m5 * bmi + m6 * GDP + m7 * cent_am + m8 * eu + m9 * na + m10 * rest_eu + m11 * sa

        st.write(f"Your life expectancy is : {round(y,1)} years.")

    elif question == 'No':
        st.write('This model requires 3 inputs, please enter when prompted:')

        adult = st.number_input('Please enter your value for "Adult Mortality": ', step=1.0)
        schooling = st.number_input('Please enter your value for "Schooling": ', step=1.0)
        developing = st.radio('Please enter your value for "Economy_status_Developing"', ('True', 'False'))

        developing = 1 if developing == 'True' else 0

        m0 = 75.8524
        m1 = -0.0637
        m2 = 0.7685
        m3 = -0.8031

        y = m0 + m1 * adult + m2 * schooling + m3 * developing

        st.write(f"Using the minimalistic model, your life expectancy is : {round(y,1)} years.")

    else:
        st.write('This is not a valid answer! Please restart to try again')

predictLifeExpectancy()
