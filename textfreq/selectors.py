words = ur"[^\u0020^\u0021^\u0022^\u0023^\u0025^\u0026^\u0027^\u002A^\u002C^\u002E^\u002F^\u003A^\u003B^\u003F^\u0040^\u005C^\u00A1^\u00A7^\u00B6^\u00B7^\u00BF^\u037E^\u0387^\u055A^\u055B^\u055C^\u055D^\u055E^\u055F^\u0589^\u05C0^\u05C3^\u05C6^\u05F3^\u05F4^\u0609^\u060A^\u060C^\u060D^\u061B^\u061E^\u061F^\u066A^\u066B^\u066C^\u066D^\u06D4^\u0700^\u0701^\u0702^\u0703^\u0704^\u0705^\u0706^\u0707^\u0708^\u0709^\u070A^\u070B^\u070C^\u070D^\u07F7^\u07F8^\u07F9^\u0830^\u0831^\u0832^\u0833^\u0834^\u0835^\u0836^\u0837^\u0838^\u0839^\u083A^\u083B^\u083C^\u083D^\u083E^\u085E^\u0964^\u0965^\u0970^\u0AF0^\u0DF4^\u0E4F^\u0E5A^\u0E5B^\u0F04^\u0F05^\u0F06^\u0F07^\u0F08^\u0F09^\u0F0A^\u0F0B^\u0F0C^\u0F0D^\u0F0E^\u0F0F^\u0F10^\u0F11^\u0F12^\u0F14^\u0F85^\u0FD0^\u0FD1^\u0FD2^\u0FD3^\u0FD4^\u0FD9^\u0FDA^\u104A^\u104B^\u104C^\u104D^\u104E^\u104F^\u10FB^\u1360^\u1361^\u1362^\u1363^\u1364^\u1365^\u1366^\u1367^\u1368^\u166D^\u166E^\u16EB^\u16EC^\u16ED^\u1735^\u1736^\u17D4^\u17D5^\u17D6^\u17D8^\u17D9^\u17DA^\u1800^\u1801^\u1802^\u1803^\u1804^\u1805^\u1807^\u1808^\u1809^\u180A^\u1944^\u1945^\u1A1E^\u1A1F^\u1AA0^\u1AA1^\u1AA2^\u1AA3^\u1AA4^\u1AA5^\u1AA6^\u1AA8^\u1AA9^\u1AAA^\u1AAB^\u1AAC^\u1AAD^\u1B5A^\u1B5B^\u1B5C^\u1B5D^\u1B5E^\u1B5F^\u1B60^\u1BFC^\u1BFD^\u1BFE^\u1BFF^\u1C3B^\u1C3C^\u1C3D^\u1C3E^\u1C3F^\u1C7E^\u1C7F^\u1CC0^\u1CC1^\u1CC2^\u1CC3^\u1CC4^\u1CC5^\u1CC6^\u1CC7^\u1CD3^\u2016^\u2017^\u2020^\u2021^\u2022^\u2023^\u2024^\u2025^\u2026^\u2027^\u2030^\u2031^\u2032^\u2033^\u2034^\u2035^\u2036^\u2037^\u2038^\u203B^\u203C^\u203D^\u203E^\u2041^\u2042^\u2043^\u2047^\u2048^\u2049^\u204A^\u204B^\u204C^\u204D^\u204E^\u204F^\u2050^\u2051^\u2053^\u2055^\u2056^\u2057^\u2058^\u2059^\u205A^\u205B^\u205C^\u205D^\u205E^\u2CF9^\u2CFA^\u2CFB^\u2CFC^\u2CFE^\u2CFF^\u2D70^\u2E00^\u2E01^\u2E06^\u2E07^\u2E08^\u2E0B^\u2E0E^\u2E0F^\u2E10^\u2E11^\u2E12^\u2E13^\u2E14^\u2E15^\u2E16^\u2E18^\u2E19^\u2E1B^\u2E1E^\u2E1F^\u2E2A^\u2E2B^\u2E2C^\u2E2D^\u2E2E^\u2E30^\u2E31^\u2E32^\u2E33^\u2E34^\u2E35^\u2E36^\u2E37^\u2E38^\u2E39^\u2E3C^\u2E3D^\u2E3E^\u2E3F^\u2E41^\u3001^\u3002^\u3003^\u303D^\u30FB^\uA4FE^\uA4FF^\uA60D^\uA60E^\uA60F^\uA673^\uA67E^\uA6F2^\uA6F3^\uA6F4^\uA6F5^\uA6F6^\uA6F7^\uA874^\uA875^\uA876^\uA877^\uA8CE^\uA8CF^\uA8F8^\uA8F9^\uA8FA^\uA92E^\uA92F^\uA95F^\uA9C1^\uA9C2^\uA9C3^\uA9C4^\uA9C5^\uA9C6^\uA9C7^\uA9C8^\uA9C9^\uA9CA^\uA9CB^\uA9CC^\uA9CD^\uA9DE^\uA9DF^\uAA5C^\uAA5D^\uAA5E^\uAA5F^\uAADE^\uAADF^\uAAF0^\uAAF1^\uABEB^\uFE10^\uFE11^\uFE12^\uFE13^\uFE14^\uFE15^\uFE16^\uFE19^\uFE30^\uFE45^\uFE46^\uFE49^\uFE4A^\uFE4B^\uFE4C^\uFE50^\uFE51^\uFE52^\uFE54^\uFE55^\uFE56^\uFE57^\uFE5F^\uFE60^\uFE61^\uFE68^\uFE6A^\uFE6B^\uFF01^\uFF02^\uFF03^\uFF05^\uFF06^\uFF07^\uFF0A^\uFF0C^\uFF0E^\uFF0F^\uFF1A^\uFF1B^\uFF1F^\uFF20^\uFF3C^\uFF61^\uFF64^\uFF65^\u10100^\u10101^\u10102^\u1039F^\u103D0^\u1056F^\u10857^\u1091F^\u1093F^\u10A50^\u10A51^\u10A52^\u10A53^\u10A54^\u10A55^\u10A56^\u10A57^\u10A58^\u10A7F^\u10AF0^\u10AF1^\u10AF2^\u10AF3^\u10AF4^\u10AF5^\u10AF6^\u10B39^\u10B3A^\u10B3B^\u10B3C^\u10B3D^\u10B3E^\u10B3F^\u10B99^\u10B9A^\u10B9B^\u10B9C^\u11047^\u11048^\u11049^\u1104A^\u1104B^\u1104C^\u1104D^\u110BB^\u110BC^\u110BE^\u110BF^\u110C0^\u110C1^\u11140^\u11141^\u11142^\u11143^\u11174^\u11175^\u111C5^\u111C6^\u111C7^\u111C8^\u111CD^\u11238^\u11239^\u1123A^\u1123B^\u1123C^\u1123D^\u114C6^\u115C1^\u115C2^\u115C3^\u115C4^\u115C5^\u115C6^\u115C7^\u115C8^\u115C9^\u11641^\u11642^\u11643^\u12470^\u12471^\u12472^\u12473^\u12474^\u16A6E^\u16A6F^\u16AF5^\u16B37^\u16B38^\u16B39^\u16B3A^\u16B3B^\u16B44^\u1BC9F^\u00BB^\u2019^\u201D^\u203A^\u2E03^\u2E05^\u2E0A^\u2E0D^\u2E1D^\u2E21^\u00AB^\u2018^\u201B^\u201C^\u201F^\u2039^\u2E02^\u2E04^\u2E09^\u2E0C^\u2E1C^\u2E20^\u201E^0-9^\s^-^\(^\)^\[^\]^\-^\{^\}^\u2001^\u2002^\u2003^\u2004^\u2005^\u2006^\u2007^\u2008^\u2009^\u200A^\u200B^\u200C^\u200D^\u200E^\u200F^\u2010^\u2011^\u2012^\u2013^\u2014^\u2015^\u2016^\u2017^\u2018^\u2019^\u201A^\u201B^\u201C^\u201D^\u201E^\u201F^\u2020^\u2021^\u2022^\u2023^\u2024^\u2025^\u2026^\u2027^\u2028^\u2029^\u202A^\u202B^\u202C^\u202D^\u202E^\u202F^\u2030^\u2031^\u2032^\u2033^\u2034^\u2035^\u2036^\u2037^\u2038^\u2039^\u203A^\u203B^\u203C^\u203D^\u203E^\u203F^\u2040^\u2041^\u2042^\u2043^\u2044^\u2045^\u2046^\u2047^\u2048^\u2049^\u204A^\u204B^\u204C^\u204D^\u204E^\u204F^\u2050^\u2051^\u2052^\u2053^\u2054^\u2055^\u2056^\u2057^\u2058^\u2059^\u205A^\u205B^\u205C^\u205D^\u205E^\u205F^\u2060^\u2061^\u2062^\u2063^\u2064^\u2066^\u2067^\u2068^\u2069^\u206A^\u206B^\u206C^\u206D^\u206E^\u206F]+"

