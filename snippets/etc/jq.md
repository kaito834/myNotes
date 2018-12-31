# Environment
- Windows 10
- jq 1.5 (Download from [here](https://stedolan.github.io/jq/download/#windows))
- MinGW including [Git for Windows](https://git-for-windows.github.io/)

# My Usage of *jq*
## Filter specific element
You can filter specific element by `.foo`. `.` means root of inputted json object, and `foo` means object key name in the root object. The value of `foo` key in the root object is outputted if you filter by `.foo`.
Example result is as below: *jq* with [AWS IP Address Ranges(ip-ranges.json)](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html). The example means to filter value of `createDate` key in the root object.

```
$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | head
{
  "syncToken": "1546032855",
  "createDate": "2018-12-28-21-34-15",
  "prefixes": [
    {
      "ip_prefix": "18.208.0.0/13",
      "region": "us-east-1",
      "service": "AMAZON"
    },
    {

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | ./jq.exe '.createDate'
"2018-12-28-21-34-15"
```

*jq* allows users to repeat `.foo` like `.foo.bar`. According to [jq manual](https://stedolan.github.io/jq/manual/#Basicfilters), *A filter of the form .foo.bar is equivalent to .foo|.bar*. You can filter the values in nested object if you filter by repeating `.foo`. For example, *jq* with `.foo.bar` filters the value of `bar` key in an object which name is `foo` in the root object.
Example result is as below: jq with [AWS IP Address Ranges(ip-ranges.json)](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html). The example means to filter value of `ip_prefix` key in first object on `prefixes` array in the root object. Please refer to [Array Index on jp manual](https://stedolan.github.io/jq/manual/#Basicfilters).

```
$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | head
{
  "syncToken": "1546032855",
  "createDate": "2018-12-28-21-34-15",
  "prefixes": [
    {
      "ip_prefix": "18.208.0.0/13",
      "region": "us-east-1",
      "service": "AMAZON"
    },
    {

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | ./jq.exe '.prefixes[0].ip_prefix'
"18.208.0.0/13"
```

## Output filter results as object or Array
When you run *jq* with combined filter with comma(`,`), *jq* combines each filter results and outputs them simply. `{}` allows you to output combined results as object. Also, `[]` allows you to output them as array. Example results are as below: jq with [AWS IP Address Ranges(ip-ranges.json)](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).
* Refer to [Object/Array construction in jq manual](https://stedolan.github.io/jq/manual/#TypesandValues)

```
$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | ./jq.exe '.createDate, .prefixes[0].ip_prefix, .prefixes[0].region'
"2018-12-28-21-34-15"
"18.208.0.0/13"
"us-east-1"

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | ./jq.exe '{"a":.createDate, "b":.prefixes[0].ip_prefix, "c":.prefixes[0].region}'
{
  "a": "2018-12-28-21-34-15",
  "b": "18.208.0.0/13",
  "c": "us-east-1"
}

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | ./jq.exe '[.createDate, .prefixes[0].ip_prefix, .prefixes[0].region]'
[
  "2018-12-28-21-34-15",
  "18.208.0.0/13",
  "us-east-1"
]
```

## Filter all elements at an array from JSON object
You can filter all elements at an arrary from JSON object by [array iterator: \[\]](https://stedolan.github.io/jq/manual/#Array/ObjectValueIterator:.[]). Example result is as below: jq with [AWS IP Address Ranges(ip-ranges.json)](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html). The example means to filter only all elements of *prefixes* array by *.prefixes[]*.

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

# Related Links
## [AWS IP Address Ranges web page](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html#jq-examples)
- Example 1. Get the creation date
  * `$ jq .createDate < ip-ranges.json`
- Example 2. Get the information for a specific region
  * `$ jq '.prefixes[] | select(.region=="us-east-1")' < ip-ranges.json`
  * [Builtin function: select](https://stedolan.github.io/jq/manual/#select%28boolean_expression%29)
- Example 3. Get all IP addresses
  * `$ jq -r '.prefixes | .[].ip_prefix' < ip-ranges.json`
- Example 4. Get all IPv6 addresses
  * `$ jq -r '.ipv6_prefixes | .[].ipv6_prefix' < ip-ranges.json`
- Example 5. Get all IPv4 addresses for a specific service
  * `$ jq -r '.prefixes[] | select(.service=="CODEBUILD") | .ip_prefix' < ip-ranges.json`
- Example 6. Get all IPv4 addresses for a specific service in a specific region
  * `$ jq -r '.prefixes[] | select(.region=="us-east-1") | select(.service=="CODEBUILD") | .ip_prefix' < ip-ranges.json`
