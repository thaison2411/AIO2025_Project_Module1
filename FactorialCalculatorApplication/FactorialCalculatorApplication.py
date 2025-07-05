import streamlit as st

USERS = {'admin'}
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

def login():
    st.title("Trang dăng nhập")
    username = st.text_input("Tên đăng nhập")
    if st.button("Đăng nhập"):
        if username:
            if username in USERS:
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.session_state.logged_in = False
                st.session_state.username = username
        else:
            st.warning("Nhập tên người dùng")

def factorial_calculator():
    st.write(f"Xin chào {st.session_state.username}!")
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    number = st.number_input("Nhập một số nguyên dương để tính giai thừa:", min_value=0, max_value=900)
    if st.button("Tính giai thừa"):
        result = fact(number)
        st.write(f"Giai thừa của {number} là: {result}")

def main():
    st.title("Ứng dụng Tính Giai Thừa")
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""

    if st.session_state.logged_in:
        factorial_calculator()
    else:
        login()

if __name__ == "__main__":
    main()