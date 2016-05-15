# Shhh <img src="./assets/librarian.png" width="70"/>
[![](https://travis-ci.org/bennybauer/shhh.svg?branch=master)](https://travis-ci.org/bennybauer/shhh)

Use Shhh app to reduce noise from your slack channels, by anonymously asking members to take the discussion to a proper channel. 
Based on [SlackPolice](https://medium.com/@farski/learn-aws-api-gateway-with-the-slack-police-ca8d636e9fc0)

<a href="https://slack.com/oauth/authorize?scope=incoming-webhook,commands&client_id=2778138625.43078290818"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>


## Usage
Install Node.js

	brew install node

Install Serverless

	npm install -g serverless

Clone this repository

	git clone https://github.com/bennybauer/Shhh.git
	

Add admin.env file to root folder:

```
AWS_DEV_PROFILE=<your aws profile>
```

Add `s-variables-common.json` file to `_meta/variables` folder:

```
{
  "project": "shhh",
  "slackAppName": "Shhh",
  "slackVerificationToken": "<your_verification_token>",
  "slackAppId": "<your_app_id>",
  "slackAppSecret": "<your_secret>",
  "slackAppRedirectUri": "</slack-oauth lambda url>"
  "slackAppWelcomePage": "<app_welcome_page>"
}
```


Create the dependencies packages:

```
pip install -t functions/vendored/ -r requirements.txt
```

Deploy it!

	sls dash deploy


###Credits###
- [SlackPolice](https://medium.com/@farski/learn-aws-api-gateway-with-the-slack-police-ca8d636e9fc0) for inspiration
- Shhh icon was made by freepik from [www.flaticon.com](http://www.flaticon.com/free-icon/book-and-glasses_68105)
