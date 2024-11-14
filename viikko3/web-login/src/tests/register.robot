*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    sara
    Set Password    OiVoi123
    Set Password Confirmation    OiVoi123
    Submit Registration Form
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    t
    Set Password    OiVoi123
    Set Password Confirmation    OiVoi123
    Submit Registration Form
    Register Should Fail With Message    Username is too short!

Register With Valid Username And Too Short Password
    Set Username    sara
    Set Password    oi1
    Set Password Confirmation    oi1
    Submit Registration Form
    Register Should Fail With Message    Password is too short!

Register With Valid Username And Invalid Password
    Set Username    sara
    Set Password    oivoivoi
    Set Password Confirmation    oivoivoi
    Submit Registration Form
    Register Should Fail With Message    Password must contain at least one non-letter character!

Register With Nonmatching Password And Password Confirmation
    Set Username    sara
    Set Password    oivoi1234
    Set Password Confirmation    oivoi123
    Submit Registration Form
    Register Should Fail With Message    Passwords do not match!

Register With Username That Is Already In Use
    Set Username    kalle
    Set Password    oivoi123
    Set Password Confirmation    oivoi123
    Submit Registration Form
    Register Should Fail With Message    User with username kalle already exists


*** Keywords ***
Register Page Should Be Open
    Title Should Be    Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To Register Page

Submit Registration Form
    Click Button    Register

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Confirmation
    [Arguments]    ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Register Should Succeed
    Page Should Contain    Welcome to Ohtu Application!
