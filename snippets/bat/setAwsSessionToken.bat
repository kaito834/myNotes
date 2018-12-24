@echo off
REM This batch allows an user to set AWS Temporary Security Credentials into environment variables
REM Also, you can find similar one liner for Linux or Mac at slideshare below:
REM https://www.slideshare.net/tetsunorinishizawa/aws-cliassume-role/12

set mfaARN=arn:aws:iam::<aws account id>:mfa/<iam user name>
set /P authCode="Input authentication code on MFA device: "

REM https://teratail.com/questions/142097
REM https://qiita.com/sksmnagisa/items/8c4c1788af44cc1dc63a
REM https://aws.amazon.com/jp/premiumsupport/knowledge-center/authenticate-mfa-cli/
REM https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html
set awsGetSessionToken=call aws sts get-session-token --serial-number %mfaARN% --token-code %authCode% --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" --output text

REM Run "for /?" and see "for" help at command prompt
for /f "usebackq tokens=1,2,3" %%a in (`%awsGetSessionToken%`) do (
  set AWS_ACCESS_KEY_ID=%%a
  set AWS_SECRET_ACCESS_KEY=%%b
  set AWS_SESSION_TOKEN=%%c
)

set mfaARN=
set authCode=
set awsGetSessionToken=
