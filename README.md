[![license](https://img.shields.io/github/license/cyb3rko/stevenblack-hosts-fortinet.svg)](https://github.com/cyb3rko/stevenblack-hosts-fortinet/blob/main/LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/cyb3rko/stevenblack-hosts-fortinet/update.yml?branch=main)](https://github.com/cyb3rko/stevenblack-hosts-fortinet/actions/workflows/update.yml?query=branch%3Amain)
[![last commit](https://img.shields.io/github/last-commit/cyb3rko/stevenblack-hosts-fortinet.svg)](https://github.com/cyb3rko/stevenblack-hosts-fortinet/commits/main)
[![commit activity](https://img.shields.io/github/commit-activity/y/cyb3rko/stevenblack-hosts-fortinet.svg)](https://github.com/cyb3rko/stevenblack-hosts-fortinet/commits/main)

# StevenBlack Hosts Trimmed

This repo is based on the awesome hosts files by StevenBlack:  
https://github.com/StevenBlack/hosts

The hosts files are optimized for usage in Fortinets FortiOS fabric connectors, as they have the following limitations:  
- support only for format without leading ip address
- maximum of 131.072 entries per file
- not supporting inline comments

The main unified hosts file as well as all alternate hosts file combinations are converted in the respective directories in [alternates](alternates).

## Modifications

A simple Python script optimizes the hosts files using the following actions:

- [Line Trimming](#line-trimming)
- [File Division](#file-division)
- [Inline Comment Extraction](#inline-comment-extraction)

### Line Trimming

Converts the original format

```
0.0.0.0 ads.facebook.com
0.0.0.0 an.facebook.com
0.0.0.0 pixel.facebook.com
```

into the new format

```
ads.facebook.com
an.facebook.com
pixel.facebook.com
```

### File Division

Divides files to have a maximum of 130.000 entries per file:

129.000 entries result in:
- hosts0 (129.000)

131.000 entries result in:
- hosts0 (130.000)  
- hosts1 (1.000)

### Inline Comment Extraction

Moves inline comments like

```
ads.facebook.com # this domain is disturbing
```

to a new line

```
# this domain is disturbing
ads.facebook.com
```
