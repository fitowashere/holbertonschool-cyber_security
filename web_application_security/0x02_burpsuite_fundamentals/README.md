0. Getting Started with Burp Suite
mandatory
Score: 100.00% (Checks completed: 100.00%)
Burp Suite stands as a cornerstone tool in web application security testing, offering a vast array of features tailored for security professionals and ethical hackers.
Your first mission is to get Burp Suite up and running, configure it for web traffic interception, and uncover hidden data within TLS certificate details.

Step 1: Downloading and Installing Burp Suite

Download Burp Suite Community Edition from the official PortSwigger website.
Follow the installation instructions for your operating system to install Burp Suite.
Launch Burp Suite and familiarize yourself with the initial setup screens.
Step 2: Starting up BurpSuite

Method 1: Proxy Setup and Certificate Installation
Upon opening Burp Suite, start a new project and navigate to the Proxy -> Options tab.
Set the Burp Suite proxy to listen on 127.0.0.1:8080 or another port of your choice.
Configure your preferred web browser to route traffic through the Burp proxy by setting the HTTP proxy to 127.0.0.1 with the port you selected.
With your browser configured, attempt to navigate to any HTTPS website. You’ll be blocked by a security warning due to the browser not recognizing Burp’s certificate.
Return to Burp Suite and navigate to Proxy -> Intercept. Ensure Intercept is off. Access http://burpsuite from your browser to download the CA certificate provided by Burp.
Install this certificate in your browser’s certificate store to avoid further security warnings.
Method 2: Open Browser
Navigate to Proxy Tab.
Click on Open Browser Button.
Step 3: DNS Resolution Configuration

Navigate to Project options -> Connections in Burp Suite and find the section titled Hostname Resolution Overrides.
Add a new record with the hostname web0x02.hbtn and the IP address provided by your container or virtual lab environment.
Step 4: Discovering the FLAG

Ensure your configured browser’s proxy settings are directing traffic through Burp Suite.
Visit https://web0x02.hbtn, allowing Burp Suite to intercept the request.
After successfully accessing the site, navigate to Project options -> TLS in Burp Suite, then to Server TLS Certificate.
Carefully examine the server certificate details presented by Burp Suite, looking for a Flag encapsulated within.
Repo:

GitHub repository: holbertonschool-cyber_security
Directory: web_application_security/0x02_burpsuite_fundamentals
File: 0-flag.txt
 
1 correction request
6/6 pts
1. Client-Side TLS Authentication with Burp Suite
mandatory
Score: 100.00% (Checks completed: 100.00%)
This task involves navigating client-side TLS authentication—a critical aspect of ensuring secure connections between clients and servers.
Upon accessing https://web0x02.hbtn, you’ll encounter a welcome screen offering a download link for a .p12 certificate.
Your mission is to correctly install this certificate within Burp Suite to authenticate and reveal hidden content guarded by TLS client authentication.

Step 1: Downloading the PKCS#12 Certificate

Visit https://web0x02.hbtn through your browser configured to use Burp Suite as its proxy.
On the welcome screen, download the .p12 certificate provided via the download link. (Or Simply through: https://web0x02.hbtn/static/web0x012.p12)
Step 2: Configuring Burp Suite with Client TLS Certificate

With the .p12 certificate downloaded, open Burp Suite and navigate to Proxy -> Options.
Scroll down to the TLS section, then click on Client TLS Certificate.
Ensure the “Override options” checkbox is selected.
Click on Add to configure a new client certificate.
In the Destination Host field, enter web0x02.hbtn.
For Certificate Type, choose “PKCS#12” from the dropdown menu.
Click Select file and browse to the location where you saved the downloaded .p12 certificate.
When prompted for a password, enter holberton, which is the password for the certificate.
Step 3: Reloading the Page to Reveal Hidden Content

After successfully configuring the client TLS certificate in Burp Suite, revisit https://web0x02.hbtn in your browser.
If everything is configured correctly, upon reloading, you should bypass the initial welcome screen and gain access to a new page—a direct result of successful client-side TLS authentication.
Repo:

GitHub repository: holbertonschool-cyber_security
Directory: web_application_security/0x02_burpsuite_fundamentals
File: 1-flag.txt
 
1 correction request
6/6 pts
2. Modifying Page Responses to Reveal Hidden Information
mandatory
Score: 100.00% (Checks completed: 100.00%)
In this task, you will delve deeper into the functionalities of Burp Suite, particularly focusing on manipulating web server responses.
By intercepting and altering responses, you’ll learn how to modify web page content in real-time.
Your objective is to reveal a hidden Flag ⛳️ on the /task2 page by spoofing the frontend through response modification.

Step 1: Intercepting the Download Request

Ensure Burp Suite is configured correctly with your browser’s proxy settings.
Visit /task2 or click the “Continue” button from the previous task’s page to navigate there.
In Burp Suite, make sure Intercept is On in the Proxy -> Intercept tab.
On the /task2 page, click the “Download” button. Burp Suite should capture the outbound request to the web server.
Step 2: Modifying the Server Response

With the request captured, click on Action in Burp Suite, then choose Do intercept -> Response to this request.
Click on Intercept is on to toggle it off, allowing you to modify the intercepted response.
In the response body, edit the content to reveal or unhide the Flag. This might involve modifying JSON while maintaining format integrity.
Once you’ve made your modifications, click Forward to send the altered response to your browser.
Step 3: Revealing the Flag

After forwarding the modified response if needed value a FLAG will reveal!
Repo:

GitHub repository: holbertonschool-cyber_security
Directory: web_application_security/0x02_burpsuite_fundamentals
File: 2-flag.txt
 
2 correction requests
6/6 pts
3. Exploring the Repeater Tool
mandatory
Score: 100.00% (Checks completed: 100.00%)
Burp Suite’s Repeater tool is pivotal for testing and tweaking requests without repeatedly interacting with the web application itself.
Your objective in this task is to utilize Repeater to guess login credentials on a page designed to mimic a router’s login portal.
By examining the request details and making educated adjustments, you’ll aim to gain unauthorized access and uncover a hidden Flag ⛳️.

Step 1: Capturing the Login Request

Navigate to /task3 or continue from the previous task’s page by clicking the “Continue” button.
Ensure that Intercept is On in Burp Suite’s Proxy -> Intercept tab.
On the /task3 page, click the designated button to initiate a login request. Once the request is captured in Burp Suite, use the shortcut Ctrl + R (or right-click and select Send to Repeater) to send it to the Repeater tool.
Step 2: Guessing Credentials with Repeater

In the Repeater tab, you’ll see the captured login request ready for modification. Based on the hint that the page uses default router credentials, attempt common combinations like admin/admin, admin/password, or similar.
Pay attention to other fields in the request, such as role and remember me options. Altering these values could impact the server’s response and might be necessary for successful authentication.
Step 3: Uncovering the Flag

Continue tweaking and resending your request as needed based on server responses until you successfully authenticate.
A successful login will reveal a success message along with a hidden Flag.
Repo:

GitHub repository: holbertonschool-cyber_security
Directory: web_application_security/0x02_burpsuite_fundamentals
File: 3-flag.txt
 
1 correction request
6/6 pts
4. The Intruder's Path to Hidden Profiles
mandatory
Score: 100.00% (Checks completed: 100.00%)
Burp Suite’s Intruder tool is engineered for automating customized attacks against web applications.
This task will have you utilize Intruder to discover hidden user profiles by automating requests with varying parameters.
Your mission is to find a specific profile ID that reveals a hidden Flag ⛳️ by systematically testing different ID values.

Step 1: Capturing the Request

Navigate to /task4 or proceed by clicking the “Continue” button from the previous task’s page.
Ensure Intercept is On in Burp Suite’s Proxy -> Intercept tab.
Click the “Refresh” button on the /task4 page to generate a request. Once captured, send it to Intruder by pressing Ctrl + I or manually via the context menu.
Step 2: Setting Up and Executing an Intruder Attack

Within the Intruder tab, go to the “Positions” section. Here, you’ll find the captured request ready for modification.
Identify and highlight the profile ID parameter in the request. Click “Add” to set this parameter as the point of attack.
Switch to the “Payloads” tab. Select “Numbers” as the payload type.
Paste the copied ID into the “From” field. Add 100 or 200 to this value and enter the result into the “To” field, setting a range for Intruder to test.
Start the attack by clicking on the “Start attack” button and observe the responses from the server.
Step 3: Identifying the Correct Profile ID

Monitor the attack’s progress and results, looking for responses with a status code of 200, indicating successful access to a profile.
Once you find a profile ID that yields a 200 response, note this ID (this profile bio contains the FLAG). It signifies access to a hidden or non-public user profile.
Step 4: Retrieving the Flag

Return to the original intercepted request in the Proxy -> Intercept tab.
Replace the profile ID in the request with the ID discovered during your Intruder attack.
Forward the modified request and then turn off Intercept.
The response should now render a hidden user profile page, unveiling the sought-after Flag.
Repo:

GitHub repository: holbertonschool-cyber_security
Directory: web_application_security/0x02_burpsuite_fundamentals
File: 4-flag.txt
 
1 correction request
6/6 pts
5. Deciphering Tokens with Sequencer
mandatory
Score: 100.00% (Checks completed: 100.00%)
Burp Suite’s Sequencer tool is designed for testing the randomness of session tokens, cookies, and other critical data that should be unpredictable and resistant to guessing attacks.
In this exercise, you’ll use Sequencer to analyze a specific cookie, hijack_session, to uncover patterns or weaknesses in how it’s generated.
Ultimately, your analysis will lead you to a valid session cookie that reveals a hidden Flag ⛳️.

Step 1: Capturing the Request

Navigate to /task5 or continue from the previous task’s page by clicking the “Continue” button.
Make sure Intercept is On in Burp Suite’s Proxy -> Intercept tab.
Once the page loads, capture this initial request and send it to the Repeater by pressing Ctrl + R or through the context menu.
Step 2: Preparing for Sequencer Analysis

In the Repeater tab, locate the Cookie header and remove the hijack_session value from the request.
Right-click on the modified request and select “Send to Sequencer.”
Step 3: Configuring and Starting Sequencer

In the Sequencer tab, ensure the tool detects the hijack_session parameter for analysis.
Before starting the live capture, enter Sequencer settings and adjust the “Throttle between requests (ms)” to 25 to regulate the pace of token generation without overwhelming the server.
Close the settings and initiate the live capture of tokens. Aim to generate around 200 tokens before halting the capture.
Step 4: Analyzing Token Pattern and Hijacking Session

After stopping the capture, export or copy the tokens into your preferred text editor for analysis.
Review the sequence of tokens to identify any discernible patterns or anomalies, such as skipped or repeating values.
Locate a skipped cookie value—this represents a valid session that can be exploited.
Replace your current session cookie in the browser (using developer tools or a cookie management extension) with the identified valid hijack_session value.
Step 5: Revealing the Flag

With the valid session cookie set, reload /task5 in your browser.
Interact with any newly accessible features or content on the page (e.g., scratching a card) to uncover the hidden Flag.
Repo:

GitHub repository: holbertonschool-cyber_security
Directory: web_application_security/0x02_burpsuite_fundamentals
File: 5-flag.txt
 
1 correction request
6/6 pts
6. `Decoder` Tab - Manipulating Base64 Encoded Bearer Tokens
mandatory
Score: 100.00% (Checks completed: 100.00%)
In the final task of this series, you’ll delve into the intricacies of Bearer Token manipulation.
By intercepting a request that includes a Bearer Token, you’ll decode, modify, and re-encode the token to escalate privileges and reveal a hidden Flag ⛳️.
This task emphasizes the importance of secure token handling and validation by web applications.

Step 1: Intercepting the Request

Navigate to /task6 or continue from the previous task by clicking the “Continue” button at the bottom of the page.
Ensure Intercept is On in Burp Suite’s Proxy -> Intercept tab.
Click the “Check All” button on the /task6 page to generate a request.
Intercept this request in Burp Suite.
Step 2: Modifying the Bearer Token

Locate the Authorization header in the intercepted request, which contains the Bearer Token.
Right-click on the token and select “Send to Decoder” or navigate to the Decoder tab and paste the token there.
Step 3: Decoding and Editing the Token

In the Decoder tab, follow these steps to decode and modify the token:
Decode the token from Base64.
Decompress the decoded data (GZIP).
You should now see a JSON object with an "admin": false value.
Edit the JSON to change "admin": false to "admin": true.
Compress the modified JSON using GZIP.
Encode the compressed data back to Base64.
Step 4: Replacing the Modified Token

Copy the newly encoded token.
Return to the Proxy -> Intercept tab, and replace the original Bearer Token in the Authorization header with your modified token.
Forward the request.
Step 5: Revealing the Flag

With the modified Bearer Token sent, monitor the application’s response for any changes or newly accessible content that indicates elevated privileges.
Look for and document the hidden Flag that is revealed as a result of your successful token manipulation.
Repo:

GitHub repository: holbertonschool-cyber_security
Directory: web_application_security/0x02_burpsuite_fundamentals
File: 6-flag.txt
 
1 correction request
6/6 pts