
## Getting started with Streamlit

**Author: Abhishek Dey**

**Date: 13 July 2025**


## Installation

```

pip3 install streamlit

```

## Create a streamlit app file

```

touch app.py

```

## How to run streamlit app

```

streamlit run app.py

```

## Commonly used streamlit commands:

* **Title**

```
st.tile("Write your title here")

```

* **Markdown**

```

st.markdown(" # Use hashtages")

```

* **Text input**

```

st.text_input("Enter your text")

```

* **Calender**

```

st.date_input("pick a date")

```


* **Slider**

```

st.slider("Pick a nuber between 0-100", 0, 100)

```

* **Radio button**

```

st.radio("select from radio buttions", options=["opt1", "opt2"])

```

* **Dropdown**

```

st.selectbox("select from drop down menu", options=["opt1", "opt2"])

```

* **File uploader**

```

st.file_uploader("upload file")

```