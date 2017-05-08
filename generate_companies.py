import json
import sqlite3
import urllib.request

def main():
    conn = sqlite3.connect('seng/server/db.sqlite3')
    curs = conn.cursor()

    for ric, name in COMPANY_NAMES:
        curs.execute('INSERT INTO server_company (ric, name) VALUES (?, ?)', (ric, name))

    conn.commit()

COMPANY_NAMES = [
    ('005490', 'POSCO'),
    ('2002', 'China Steel Corporation'),
    ('3668', 'CHINALCO-CMC'),
    ('600019', 'Baosteel'),
    ('600362', 'JCCL'),
    ('601898', 'CHINA COAL ENERGY'),
    ('AAL', 'Anglo American plc'),
    ('ABI', 'Anheuser-Busch InBev SA/NV'),
    ('ADRO', 'Adaro Energy Tbk.'),
    ('AGRO3', 'BrasilAgro - Companhia Brasileira de Propriedades Agrícolas'),
    ('ANTO', 'Antofagasta plc'),
    ('APF', 'Anglo Pacific Group plc'),
    ('ASR', 'Alacer Gold Corp.'),
    ('AZN', 'AstraZeneca PLC'),
    ('BARC', 'Barclays PLC'),
    ('BCI', 'BC Iron Limited'),
    ('BHP', 'BHP Billiton Limited'),
    ('BLT', 'BHP Billiton plc'),
    ('BP', 'BP p.l.c.'),
    ('CBA', 'Commonwealth Bank of Australia'),
    ('EVN', 'Evolution Mining Limited'),
    ('FIBR3', 'Fibria Celulose S.A.'),
    ('FMG', 'Fortescue Metals Group Limited'),
    ('GLEN', 'Glencore Plc'),
    ('GSK', 'GlaxoSmithKline plc'),
    ('HMSO', 'Hammerson plc'),
    ('HSBA', 'HSBC Holdings plc'),
    ('IGO', 'Independence Group NL'),
    ('KMD', 'Kathmandu Holdings Limited'),
    ('MQG', 'Macquarie Group Limited'),
    ('MS', 'CAS.ETF MS.NET INAV'),
    ('MYR', 'Myer Holdings Limited'),
    ('NCM', 'Newcrest Mining Limited'),
    ('NOVN', 'NOVARTIS N'),
    ('NUF', 'Nufarm Limited'),
    ('OGC', 'OceanaGold Corporation'),
    ('OIBR3', 'Oi S.A.'),
    ('ORG', 'Origin Energy Limited'),
    ('OZL', 'OZ Minerals Limited'),
    ('RBS', 'The Royal Bank of Scotland Group plc'),
    ('RIO', 'Rio Tinto Limited'),
    ('RR', 'Rolls-Royce Holdings plc'),
    ('S32', 'South32 Limited'),
    ('SASY', 'SANOFI'),
    ('SFR', 'Sandfire Resources NL'),
    ('SIP', 'Sigma Pharmaceuticals Limited'),
    ('SMR', 'Stanmore Coal Limited'),
    ('STO', 'Santos Limited'),
    ('SYNN', 'SYNGENTA N'),
    ('VALE5', 'Vale S.A.'),
    ('WBC', 'Westpac Banking Corporation'),
    ('WOR', 'WorleyParsons Limited'),
    ('YAL', 'Yancoal Australia Ltd'),
    ('1088', 'China Shenhua Energy Company Limited'),
    ('2899', 'Zijin Mining Group Company Limited'),
    ('4188', 'AMCAD BIOMED CORPO TWD10'),
    ('600188', 'YANZHOU COAL'),
    ('601088', 'China Shenhua'),
    ('601899', 'Zijin Mining'),
    ('ABBV', 'ABBVIE'),
    ('ABX', 'Barrick Gold Corporation'),
    ('AGO', 'Atlas Iron Limited'),
    ('ANZ', 'Australia and New Zealand Banking Group Limited'),
    ('ATLN', 'ACTELION N'),
    ('BDR', 'Beadell Resources Limited'),
    ('FNV', 'Franco-Nevada Corporation'),
    ('HBM', 'Hudbay Minerals Inc.'),
    ('IHG', 'InterContinental Hotels Group PLC'),
    ('NAB', 'National Australia Bank Limited'),
    ('NOBG', 'Noble'),
    ('NPT', 'NetPlay TV plc'),
    ('OR', 'Osisko Gold Royalties Ltd.'),
    ('OSH', 'Oil Search Limited'),
    ('RDSA', 'Royal Dutch Shell plc'),
    ('RRL', 'Regis Resources Limited'),
    ('SEA', 'Seabridge Gold Inc.'),
    ('SLW', 'Silver Wheaton Corp.'),
    ('SUZB5', 'Suzano Papel e Celulose S.A.'),
    ('VRX', 'Valeant Pharmaceuticals International, Inc.'),
    ('WHC', 'Whitehaven Coal Limited'),
    ('WPL', 'Woodside Petroleum Ltd'),
    ('4612', 'Nippon Paint Holdings Co Ltd'),
    ('8002', 'Marubeni Corp'),
    ('8058', 'Mitsubishi Corp'),
    ('AA', 'Alcoa Corp'),
    ('ANRZQ', 'Alpha Natural Resources, Inc.'),
    ('ARI', 'Arrium Ltd'),
    ('BAC', 'Bank of America Corp'),
    ('BAS', 'Basic Energy Services Inc'),
    ('BG', 'BG Group'),
    ('BLDR', 'Builders FirstSource Inc'),
    ('CGIX', 'Cancer Genetics Inc'),
    ('CLF', 'Cliffs Natural Resources Inc'),
    ('CMG', 'Chipotle Mexican Grill Inc'),
    ('CVX', 'Chevron Corporation'),
    ('DD', 'E I du Pont de Nemours and Co'),
    ('DOW', 'Dow Chemical Co'),
    ('DWA', 'DreamWorks Animation LLC'),
    ('FCX', 'Freeport-McMoRan Inc'),
    ('FLR', 'Fluor Corp'),
    ('GLUU', 'Glu Mobile Inc'),
    ('GS', 'Goldman Sachs Group Inc'),
    ('ICON', 'Iconix Brand Group Inc'),
    ('JPM', 'JPMorgan Chase & Co'),
    ('KHC', 'Kraft Heinz Co'),
    ('LND', 'Brasilagro Companhia Brasileira de Propriedades Agricolas'),
    ('MNST', 'Monster Beverage Corp'),
    ('MRNS', 'Marinus Pharmaceuticals Inc'),
    ('PATAQ', 'Patriot Coal Corp'),
    ('PICK', 'iShares MSCI Global Metals & Mining Producers ETF'),
    ('QRVO', 'Qorvo Inc'),
    ('RF', 'REFFIND LIMITED'),
    ('ROD', 'Sportech PLC'),
    ('STI', 'SunTrust Banks Inc'),
    ('STMP', 'Stamps.Com Inc'),
    ('TCKB', 'Teck Resources Ltd'),
    ('TISC', 'Tata Steel Ltd'),
    ('TRGP', 'Targa Resources Corp'),
    ('TRUE', 'TrueCar Inc'),
    ('VALE', 'Valecha Engineering Ltd'),
    ('WIBC', 'Wilshire Bancorp Inc'),
    ('WTW', 'Weight Watchers International Inc'),
    ('XME', 'SPDR S&P Metals & Mining ETF'),
    ('YOKU', 'Youk Tudo Inc'),
    ('5411', 'JFE Holdings, Inc.'),
    ('8053', 'Sumitomo Corp'),
    ('9179', 'Kawasaki Kinkai Kisen Kaisha Ltd'),
    ('ARWR', 'Arrowhead Pharmaceuticals Inc'),
    ('BABA', 'Alibaba Group Holding Ltd'),
    ('BBCN', 'Bancorp Inc'),
    ('BLK', 'BlackRock, Inc.'),
    ('BTU', 'Peabody Energy Corp'),
    ('CENX', 'Century Aluminum Co'),
    ('CIG', 'Companhia Energetica de Minas Gerais CEMIG'),
    ('CMP', 'Compass Minerals International, Inc.'),
    ('DATA', 'Tableau Software Inc'),
    ('DIS', 'Walt Disney Co'),
    ('DVN', 'Devon Energy Corp'),
    ('EPD', 'Enterprise Products Partners LP'),
    ('EYES', 'Second Sight Medical Products Inc'),
    ('GMCR', 'Keurig Green Mountain Inc'),
    ('HL', 'Hecla Mining Co'),
    ('HZNP', 'Horizon Pharma PLC'),
    ('JNJ', 'Johnson & Johnson'),
    ('KBIO', 'KaloBios Pharmaceuticals Inc'),
    ('KKR', 'KKR & Co LP'),
    ('KMI', 'Kinder Morgan Inc'),
    ('LXRX', 'Lexicon Pharmaceuticals Inc'),
    ('MRVL', 'Marvell Technology Group Ltd'),
    ('MW', "Men's Wearhouse Inc"),
    ('NVDA', 'NVIDIA Corp'),
    ('OIBR', 'Oi SA'),
    ('PAOC', 'Pan Ocean Container Supplies Ltd.'),
    ('PBY', 'Pep Boys'),
    ('REDY', "Dr.Reddy's Laboratories Ltd"),
    ('RGLD', 'Royal Gold Inc'),
    ('RS', 'Reliance Steel & Aluminum Co'),
    ('SAMNE', 'Samarco Mineracao SA'),
    ('SHAK', 'Shake Shack Inc'),
    ('SONA', 'Sona Petroleum Bhd'),
    ('STLD', 'Steel Dynamics Inc'),
    ('TNGO', 'Tangoe Inc'),
    ('TRIP', 'TripAdvisor Inc'),
    ('TTWO', 'Take Two Interactive Software Inc'),
    ('WLTGQ', 'New Wei Inc'),
    ('X', 'United States Steel Corp'),
    ('XOM', 'Exxon Mobil Corp'),
    ('YHOO', 'Yahoo! Inc'),
    ('ZSPH', 'ZS Pharma Inc'),
    ('HOT', 'Starwood Hotels & Resorts Worldwide Inc.'),
    ('TIGERBRD', 'Tiger Branded Consumer Goods PLC'),
    ('XTAXS', 'Glencore Canada Corporation')
]

if __name__ == '__main__':
    main()
