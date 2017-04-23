# Environment
- Windows 10
- jq 1.5 (Download from [here](https://stedolan.github.io/jq/download/#windows))
- MinGW including [Git for Windows](https://git-for-windows.github.io/)

# My Usage of *jq*
## Filter all elements at an array from JSON object
You can filter all elements at an arrary from JSON object by [array iterator: \[\]](https://stedolan.github.io/jq/manual/#Array/ObjectValueIterator:.[]). Example result is as below: jq with [AWS IP Address Ranges(ip-ranges.json)](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html). The example means to filter only all elements of *prefixes* array by *.prefixes[]*.

By the way, there are 3 examples at [AWS IP Address Ranges web page](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html#jq-examples).
- Example 1. Get the creation date
- Example 2. Get the information for a specific region
  * [Builtin function: select](https://stedolan.github.io/jq/manual/#select%28boolean_expression%29)
- Example 3. Get all IP addresses

```
$ jq-win64.exe --version
jq-1.5

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe .prefixes[]
{
  "ip_prefix": "13.32.0.0/15",
  "region": "GLOBAL",
  "service": "AMAZON"
}
{
  "ip_prefix": "13.54.0.0/15",
  "region": "ap-southeast-2",
  "service": "AMAZON"
}
(snip)
```

## Output raw string, non-escaped string
*jq* with no options outputs quoted strings. But, *jq* with [-r/--raw-output](https://stedolan.github.io/jq/manual/#Invokingjq) option outputs non-quoted strings. Example result is as below: jq with [AWS IP Address Ranges(ip-ranges.json)](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).

```
$ jq-win64.exe --version
jq-1.5

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe '.prefixes[0:3] | .[].ip_prefix'
"13.32.0.0/15"
"13.54.0.0/15"
"13.56.0.0/16"

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe -r '.prefixes[0:3] | .[].ip_prefix'
13.32.0.0/15
13.54.0.0/15
13.56.0.0/16
```

## List keys in JSON object
You can list only keys from JSON object by builtin function [keys or keys_unsorted](https://stedolan.github.io/jq/manual/#keys,keys_unsorted). Example result is as below: jq with [AWS IP Address Ranges(ip-ranges.json)](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).
```
$ jq-win64.exe --version
jq-1.5

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe 'keys'
[
  "createDate",
  "ipv6_prefixes",
  "prefixes",
  "syncToken"
]

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe 'keys_unsorted'
[
  "syncToken",
  "createDate",
  "prefixes",
  "ipv6_prefixes"
]
```

## Convert JSON object into CSV format
*jq* with [@csv syntax](https://stedolan.github.io/jq/manual/#Formatstringsandescaping) can output an array as CSV format. *jq* allow you to parse JSON object and generate modified array. Then, the modified array is outputted as CSV by @csv syntax. You should execute *jq* with '[-r](https://stedolan.github.io/jq/manual/#Invokingjq)' option when use @csv syntax. Because *jq* without '-r' option output quoted strings at each fields in CSV format.

Example result is as below: jq with [AWS IP Address Ranges(ip-ranges.json)](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).
```
$ jq-win64.exe --version
jq-1.5

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe '{syncToken, createDate, prefixes: .prefixes[]}' | head -25
{
  "syncToken": "1492807931",
  "createDate": "2017-04-21-20-52-11",
  "prefixes": {
    "ip_prefix": "13.32.0.0/15",
    "region": "GLOBAL",
    "service": "AMAZON"
  }
}
{
  "syncToken": "1492807931",
  "createDate": "2017-04-21-20-52-11",
  "prefixes": {
    "ip_prefix": "13.54.0.0/15",
    "region": "ap-southeast-2",
    "service": "AMAZON"
  }
}
{
  "syncToken": "1492807931",
  "createDate": "2017-04-21-20-52-11",
  "prefixes": {
    "ip_prefix": "13.56.0.0/16",
    "region": "us-west-1",
    "service": "AMAZON"
Error: writing output failed: Invalid argument

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe '{syncToken, createDate, prefixes: .prefixes[]} | [.syncToken, .createDate, .prefixes.ip_prefix, .prefixes.region, .prefixes.service]' | head -15
[
  "1492807931",
  "2017-04-21-20-52-11",
  "13.32.0.0/15",
  "GLOBAL",
  "AMAZON"
]
[
  "1492807931",
  "2017-04-21-20-52-11",
  "13.54.0.0/15",
  "ap-southeast-2",
  "AMAZON"
]
[
Error: writing output failed: Invalid argument

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe -r '{syncToken, createDate, prefixes: .prefixes[]} | [.syncToken, .createDate, .prefixes.ip_prefix, .prefixes.region, .prefixes.service] | @csv'  | head
"1492807931","2017-04-21-20-52-11","13.32.0.0/15","GLOBAL","AMAZON"
"1492807931","2017-04-21-20-52-11","13.54.0.0/15","ap-southeast-2","AMAZON"
"1492807931","2017-04-21-20-52-11","13.56.0.0/16","us-west-1","AMAZON"
"1492807931","2017-04-21-20-52-11","13.58.0.0/15","us-east-2","AMAZON"
"1492807931","2017-04-21-20-52-11","13.112.0.0/14","ap-northeast-1","AMAZON"
"1492807931","2017-04-21-20-52-11","13.124.0.0/16","ap-northeast-2","AMAZON"
"1492807931","2017-04-21-20-52-11","13.126.0.0/15","ap-south-1","AMAZON"
"1492807931","2017-04-21-20-52-11","13.210.0.0/15","ap-southeast-2","AMAZON"
"1492807931","2017-04-21-20-52-11","13.228.0.0/15","ap-southeast-1","AMAZON"
"1492807931","2017-04-21-20-52-11","23.20.0.0/14","us-east-1","AMAZON"
Error: writing output failed: Invalid argument
```

### Reference
- [jqを使ってJSONをCSVに変換するいくつかの例。 - Jupitris on Laboratory](http://jupitrisonlabs.hatenadiary.jp/entry/20151127/1448606090) (in Japanese)
