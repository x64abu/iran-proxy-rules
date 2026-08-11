# Iran Proxy Rules

This repository will contain routing rules for the Shadowrocket client and Xray-based clients.
This repository is a fork of [bootmortis/iran-hosted-domains](https://github.com/bootmortis/iran-hosted-domains), with several modifications and additional routing rules.

A lot of services and domains are outside of Iran and they are restricted or blocked,
for accessing this service you need to use VPN or proxies with tunneling option, apart from these problems, when we use
proxies the domestic services are unavailable because our IP is not in Iran; for bypassing these issues we gathered a list of
Iranian domains and services to help our people bypass this situation.

## Disclaimer

This repository is a compiled list of public information about websites hosted in Iran. It is intended for informational purposes only and is not intended to provide guidance on how to connect to or create or manage a virtual private network (VPN). The content in this repository is provided as-is and we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability of the information contained in this repository. Any reliance you place on such information is strictly at your own risk. We will not be liable for any errors or omissions in the information or for any losses, damages, or other liabilities that may arise from its use. Please use caution and consult with a qualified professional before using any information from this repository.


## Categories

-   `all`: a combination of `other` and `tld-ir`, should be used as `direct`.
-   `ads`: Iran-related advertising services that need to be `blocked`.
-   `proxy`: Iran-related domains that are blocked inside of iran and need to be `proxied`.
-   `ir`: handpicked `.ir` domains, use as `direct`.
-   `other`: non `.ir` domains, use as `direct`.
-   `tld-ir`: all `.ir` domains, use as `direct`.

## Files

You can always find the latest version of these files in the [release page][link-release].  
You can click on app name to see the usage instructions.  
Also, for each file there is a `.sha256` file that contains sha256 hash of that file.


## Sources & Acknowledgements

-   Iran Domains:
    -   [ITO GOV](https://eservices.ito.gov.ir/page/iplist) - [Mirror](https://github.com/bootmortis/ito-gov-mirror)
    -   [Enamad](https://enamad.ir/DomainListForMIMT) - [Mirror](https://github.com/bootmortis/enamad-mirror)
    -   [ADSL TCI](https://adsl.tci.ir/panel/sites)
    -   [V2fly Domain List Community](https://github.com/v2fly/domain-list-community) (MIT License)
    -   [Iran Web and Mobile Festival](https://directory.iwmf.ir/) - [Mirror](https://github.com/Chocolate4U/iwmf.ir-Mirror) (MIT License)
    -   [Custom List][link-custom]
-   ADs:
    -   [uBOPa - uBO Parsi filter list](https://github.com/nimasaj/uBOPa) (MIT License)

If you know of any other source, or you found a website that isn't here, please open
an [issue][link-issues] or add that specific website to [custom_domains.py][link-custom] and make a [PR][link-pr].

## How does it work?

A Python script is executed by Github Action and generates files that are on the release page.

[link-custom]: src/data/custom_domains.py
[link-pr]: ../../pulls
[link-issues]: ../../issues/new?assignees=&labels=enhancement&template=request-for-domain-addition-removal.md&title=Add%2FRemove+%60example.com%60
[link-release]: ../../releases/latest
