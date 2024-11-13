*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Input Text    username    sara
    Input Text    password    OiVoi123
    Input Text    password_confirmation    OiVoi123
    Click Button    Register
    Page Should Contain    Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Input Text    username    t
    Input Text    password    OiVoi123
    Input Text    password_confirmation    OiVoi123
    Click Button    Register
    Page Should Contain    Username is too short!

Register With Valid Username And Too Short Password
    Input Text    username    sara
    Input Text    password    oi1
    Input Text    password_confirmation    oi1
    Click Button    Register
    Page Should Contain    Password is too short!

Register With Valid Username And Invalid Password
    Input Text    username    sara
    Input Text    password    oivoivoi
    Input Text    password_confirmation    oivoivoi
    Click Button    Register
    Page Should Contain    Password must contain at least one non-letter character!

Register With Nonmatching Password And Password Confirmation
    Input Text    username    sara
    Input Text    password    oivoi1234
    Input Text    password_confirmation    oivoi123
    Click Button    Register
    Page Should Contain    Passwords do not match!

Register With Username That Is Already In Use
    Input Text    username    kalle
    Input Text    password    oivoi123
    Input Text    password_confirmation    oivoi123
    Click Button    Register
    Page Should Contain    User with username kalle already exists


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To Register Page
