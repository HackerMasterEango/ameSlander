
from youtube_transcript_api import YouTubeTranscriptApi


videos = [
'VupT9JCJaOY',
'IT7mfF97m3w',
'ojUJwXGYfZ4',
'-Om7tdfSCCs',
'T17JbKs2-y4',
'crXBpKOLCcY',
'FSwUyuy8t4g',
'GpVDj43ioMo',
'DB4w8q9Iohc',
'A3gNb5PGdKA',
'aC-cJ3WI-HU',
'6nEH6xqwqb0',
'Hrse0RUygcE',
'VAgn-bhgXeM',
'umOghkJvrpQ',
'NZ-oGtVFpVA',
'zkbXdXbs8vk',
'CLvdLn_S4uA',
'9JNwpwvd9qQ',
'lvJz679M6aE',
'bZghtnL3y3k',
'vckOfHMj0ao',
'VdzsyqaPf_0',
'-M2BKL3KU9s',
'skSmTEnAyGk',
'4W2Ulbis_SE',
'98Bk7nmK-w8',
'et8HYdSoQ-Q',
'oRMh4sP4J4s',
'N7--hFe2-Ng',
'yS0XtBrM2A8',
'2WRA7HBcvTU',
'YyH_tu3ol_c',
'NGrBBtVMN8E',
'2iXo0YDhoCA',
'OJRdtLd7xfE',
'Pqox9-28ZD0',
'wSmNK842gs8',
'lebB0-8IWtA',
'OGF6_Zoz0Eo',
'6QlHoKiFiA8',
'JKG7OToMSd4',
'sRBLyvWECvI',
'yH_2jN0aY2w',
'QpDf8Mcukoc',
'lFp1z7yIfIs',
'GsC5UDZq-3o',
'41jBh3ueyBs',
'4frqNAKQgaw',
'GkcY1yJ4z3c',
'h38izNV5ZCo',
'Fwx9HyfJoSw',
'Nw-zERkXZRk',
'5PUpgRGdpUw',
'54_JifG65ec',
'H6AqJ4ocIFk',
'50iP62tGsAM',
'tK_mD6Z_LA4',
'PfsP2lkFv-Q',
'FWVMKxLkoSU',
'ewss-AjRo7Y',
'_8X4cvg7N7M',
'VNel79gPOZI',
'19KsAtg-pR0',
'Dtj-Hkc7R0Y',
'72o--QWfufg',
'qR10vljeVoo',
'pq8hUlVP6u0',
'mFURRY0W29U',
'Gwh8wo-3HMw',
'gGbXkos5E3o',
'N9G9FfNP20g',
'hD6LwW7Zkf8',
'_PCex8qn0Io',
'nQLfdu5KZSA',
'NuMBNglZByo',
'2tQlSBCGwxg',
'WcXmdXtEVnc',
'7g0cqKTJxuE',
'nz-nmF4ByNI',
'SgQFnJFQmnw',
'v16pVEBF6I8',
'dI2Csaks9Ew',
'65lSJKzQ9f4',
'kcGhMnL2l2c',
'z4BB-oUmT5A',
'Hq9BBxGqyCY',
'CfXXwpePJGE',
'rD2eOy0BoMY',
'4ieyz_mFw-A',
'cRMaqApzVXg',
'P7AQO14NFS8',
'2k61CPt_1Zo',
'ywuO4XABCeA',
'vLSfo0tdIgU',
'l7cVX6ak86A',
'bQVAyZm76gM',
'SYwwiO52ndY',
'2cLikuqHlfc',
'JVy-Dv0hl3g',
'GIRO-554Lbg',
'7gkr1cB0OIc',
'-su7x7Crkh8',
'1aThp9samdc',
'x7znd2nBF24',
'zjTBUGgwuns',
'f2lYmGRQq9M',
'afnXlbleXS0',
'A8vq_XkX5bM',
'-rjfq4VX6lQ',
'ipZOd9ESdlo',
'dMnCBL40Bfg',
'wVD6Mm4o_RE',
'FY1XXOJmgDo',
'MRNRsXNHTkQ',
'9rCRhTrEpDE',
'1w0Jb9cr0xs',
'cs3DIupQEnQ',
'uh70V8FcWio',
'6oiquuSV3Ic',
'ltBu2XKnIKI',
'WeWtrHqLfPY',
'ZSrU5DnCnLs',
'JZjuS793OyE',
'NHeNsPUEIfg',
'N_b0kwl1abE',
'0AI7J0uxKv0',
'gKDfPuTkh0U',
'SJtutOtPiCA',
'9QViCV_INQM',
'QHzz7Blske4',
'-nqrS-gHB9Q',
'Aj0lxOOLrPI',
'TfgYuM0gUDk',
's15iykTq7ZE',
'-ayCKHL_BAw',
'ThJfcb7r14s',
'R8GpI0DxiMo',
'mu2ZPKtWMGY',
'aYMa4MQv5OA',
'RbFmqjHO3LE',
'CxbODUqwbww',
'ccRBmjw7DW8',
'aH23HxAdtw8',
'_AbZB1uuVjA',
'Z_BSMJiiYg4',
'Q_3ky2VQu6g',
'ARaFgXeAUWI',
'FJgfZUhFa7E',
'1pHcNzHJ_BE',
'9bZFbNv7c0E',
'Y5t-sNYgxDg',
'DFFZgpZv-JQ',
'E-YsTbnfpbI',
'-R7WzBchK7s',
'QLXTlOhmVO0',
't-PKCiAsPfk',
'-Q7g6PvK22o',
'zVYvskrKKaM',
'GnmJ5htzxfY',
'9PTgx7yBhwY',
'g8cM3yzgRP8',
'HL4t7MefeC4',
'WlbibYUaCUQ',
'Y20iZ_jUF0s',
'Y39ZMQKbLs0',
'7Ps8TNdh2W0',
'5KsfD-ucQEk',
'PrdVfsVzDOI',
'iO6xEwdXk_A',
'Mory0I9vXtI',
'eALSNrEkQY0',
'SX35n8Vmyqg',
'O0syH7ZzzsA',
'nELfxuOWjBQ',
'vW0ZHW64Vtk',
'MycK0pkIqns',
'LHGRcNIW4c8',
'-J1cBHhjciw',
'7QtmW1XQUl0',
'aW7MNZWj5eo',
'0Qygvs0rG50',
'F92OE63cG-U',
'JZtOJPmVt_A',
'a6fSve7RVhw',
'z5WCQJJtKFs',
'oOnDKe8hO0s',
'i4FsF0ViM2s',
'25--SXFoFP0',
'C6WsvUe0NWw',
'VVNTUCzh4E0',
'okuGibvAAJE',
'oINJuZcFdRM',
'ID71qISv2rU',
'YoPz0zz3K9U',
'3IBHjBYBFFA',
'16u2G57o6GE',
'elnwDuGqc3I',
'8fX_KzrrzcA',
'y73vNPX6DqA',
'y73vNPX6DqA',
'r2kN4QFXqWo',
'-OIP3bS2x_g',
'iD7cqNMosJI',
'TErNPEs4_uc',
'cSHMqA9zfkA',
'6yOf2HokR9s',
'CqCEa0nuUxg',
'YTVJSZL3Bp8',
'Ug3_rdG8oK8',
'E0GkIuLwaYQ',
'et3Mq2bf44Y',
'eJK_VQHeHKY',
'BxY2zb8tPyg',
'NKcT0iBwf3E',
'Oc-2g9IGq7k',
'HYxbeOdnGjw',
'FMnPyvgGShI',
'vE4XIyeFWik',
'GaM46Jp6jdg',
'95jYNgLg_yQ',
'm0u7OsyXUGk',
'ja8Mo6aKXxk',
'OE-BmnlBKJ8',
'rhCC-uawQy8',
'E4fol47EM50',
'Is-Z9NYqHmY',
'0ruxO4TmMng',
'BQpSMaDz8Y8',
'yzdYdFCm9Yg',
'99A-sYbD__I',
'xM42-Sya8Hg',
'uW7lXW2p4D8',
'upZqhkVq5iA',
'f3zWbV4joAE',
'WN5A9DIlmvc',
'eXQK45AcMoU',
'3qjHreL-ViA',
'6VBQyNHxlR8',
'vqqjksBRaF0',
'q1fipTr_OsI',
'NtGAJx3yW60',
'0Bpot8Jvbf4',
'uu8t0NGySzg',
'uO0fzCt3yNA',
'lcj9lF53VvA',
'QKm6KDC6CTU',
'_2jtFfRfGA4',
'FUPHqZT-Tkg',
'dASLzQvk4Qw',
'qTkbIGZAEaQ',
'EQKFhOUixfk',
'SUMwWqGrgC4',
'IepDIOKlXKc',
'h5Ao5aIJ8SY',
'NKhdTqn-EJ0',
'xop_KX-7Als',
'icT5nkMuo_s',
'ijcY54nePYE',
'Zx5b-_fmA8M',
'UhG_BItojWg',
'sDCPbXXgPK8',
'nEKyz1n83Q0',
'KhIH0GhzrNU',
'xD8zsjpah3A',
'rWWyO4eZ2dw',
'9GgmxoKZQQg',
'9H84jHYgvHE',
'w4auNHelA-k',
'CZG0-I0xoS4',
'E8VqyJYCTtc',
'68vrumiFx4c',
'e4Tl8BFPmmI',
'spxFKhGAZMw',
'sTCjyHkPN28',
'4Ffc4qh8hL8',
'Lovz9hosw7Q',
'DKrM4_hc70Y',
'236t8rRwNpA',
'QCVgdQr8wuw',
'1fpQW7TE1Fs',
'oACehjJaxLs',
'3HcN3Tl65ds',
'_92nbvxRi8g',
'P-MKXDNVO3g',
'ssaLVgX2SWo',
'jiOMr4Kx7oQ',
'5efPwIA_PQQ',
'lYwIKijwXSI',
'w-3rhz9NwfA',
'LPHmXGJw9jI',
'DtoPcFdbS2k',
'CZgCKkwFKck',
'bvXaozXgoiE',
'dlDhy0q8n0s',
'FF1sO1EhopY',
'kcrr1IwaY8s',
'DYF24dvP_J0',
'DrWGUBDoYqQ',
'1dO7lcQb5D4',
'a-LP6UT8TyQ',
'48ezwzLEWGU',
'KtwDxHC2hCs',
'o5AFEwAd0NE',
'OT3O2SG2TBk',
'F9T7DRYzxKE',
'tRlMsPBxIBs',
'Yi2XFtXr4Jo',
'c4MPrqARQOY',
'RNlRAvY-8ZA',
'9EEZrxnX9BU',
'9EkK-otanA4',
'VNv0EE9Fc84',
'5NEUn1zgMME',
'iPyE1YhoP40',
'-NhCxGDgmag',
'ZA4xHo_FvyY',
'EWevQ37KzCQ',
'wYPk4XNZgtw',
'416oHUbc59A',
'6eDwDvajPJc',
'YGzAP4fvG1g',
'RQOE6Z1ajYc',
'HhBed7724S8',
'blLDxuA9wVU',
'EeC6OHBRFTc',
'a85qBNgWFJM',
'VIdtsPO30vs',
'WrywL4t1P2Y',
'G8Byj4vFtHk',
'-25bgKIuH2s',
'SanTjOArUt4',
'IKiwczRMeXs',
'VOO8GlUje4U',
'It_FypkR_Bc',
'IJIrgsjsMhQ',
'Pi3EWsaMGS0',
'nFEI1VTZeos',
'z1hxCh9IIkg',
'AvFdDk4aFQ4',
'NHyNILbp9J8',
'vYhv44NfTiw',
'rH8uCzwHoRU',
'3sksEHVHNQU',
'U6tyuTgKgIs',
'Fem2_WC2FK4',
'4dKJ9vjhgEA',
'Jj2JFtU7c78',
'4ogOQ5EnJn0',
'ztM7Q-Qm-CQ',
'Nn9AGOrDNDQ',
'983K4eyK16A',
'0iSKEkdDAKA',
'lnU6Nq-o7OM',
'huaoaKsAXwI',
'_XzJP9MIugs',
'xcdlTH2FZEo',
'uRRQA3kzZ6k',
'QPs1FZSOzR8',
'5gs-58be1xE',
'hi-M24buD-o',
'se-D1R_lNTw',
'2DMWG9b-jdw',
'nDsE2HWniXY',
'sd79jNyc1lg',
'BwdZ0cCvtho',
'K86Lky4gnFI',
'pSQytMc4d5s',
'hcmI3ojzXJM',
'ZMaiB89B6Y0',
'zYYXgCiCEEk',
'MhcIdutP0L8',
'Q-KSm_DBP8w',
'-V17IYPaSRo',
'DYTLbDffouA',
'YGzAP4fvG1g',
'b8Dz-z5MyxI',
'KH30_VHmEfw',
'VMtcyYQCXlQ',
'IC_zuFwz0q8',
'Z-nP-w4XCk4',
'EaqXgBrARfU',
'mBuvlN5PINs',
'vyxlUvReKWM',
'hLMCvW96564',
'wSm0QC8JBdE',
'_T5q-IZO7ic',
'Qyq3FGmI0Ms',
'mUJawV1I6Y8',
'5Pmid4VfFmM',
'GvsYMU7CVqc',
'UMgiadw0m0o',
'DrQQc4Z9BJ0',
'cOH1vx1WhX0',
'oYXO0zc-rO4',
'ZE-9Q6uPioQ',
'2L6Bw1KsfuA',
'CW_mbwXqGHE',
'W1pzmL5jQ-0',
'z80SD3ACg6o'
]



problematic_words_and_phrases = ["copium"]




for videoId in videos:
  try:
    transcript = YouTubeTranscriptApi.get_transcript(videoId)
    results = list(filter(lambda x: any(word in x[videoId]['text'] for word in problematic_words_and_phrases), map(lambda x: { videoId: x }, transcript)))
    if results:
      print(results)
  except:
    continue



