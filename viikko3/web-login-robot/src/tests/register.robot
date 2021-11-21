*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go to Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallekalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go to Register Page
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  k
    Set Password Confirmation  k
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Credentials
    Register Should Fail With Message  Passwords not matching

Login After Successful Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Go To Login Page
    Set Username  k
    Set Password  kalle123
    Submit Login
    Login Should Fail With Message  Invalid username or password
    Go to Register Page


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}