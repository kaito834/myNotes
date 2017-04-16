# Environment
- Windows 10
- jq 1.5 (Download from [here](https://stedolan.github.io/jq/download/#windows))

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
