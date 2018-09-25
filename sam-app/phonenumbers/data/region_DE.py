"""Auto-generated file, do not edit by hand. DE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_DE = PhoneMetadata(id='DE', country_code=49, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-35-9]\\d{3,14}|4(?:[0-8]\\d{3,12}|9(?:[0-37]\\d|4(?:[1-35-8]|4\\d?)|5\\d{1,2}|6[1-8]\\d?)\\d{2,8})', possible_length=(4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), possible_length_local_only=(3, 4)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2\\d{5,13}|3(?:0\\d{3,13}|2\\d{9}|[3-9]\\d{4,13})|4(?:0\\d{3,12}|[1-8]\\d{4,12}|9(?:[0-37]\\d|4(?:[1-35-8]|4\\d?)|5\\d{1,2}|6[1-8]\\d?)\\d{2,8})|5(?:0[2-8]|[1256]\\d|[38][0-8]|4\\d{0,2}|[79][0-7])\\d{3,11}|6(?:\\d{5,13}|9\\d{3,12})|7(?:0[2-8]|[1-9]\\d)\\d{3,10}|8(?:0[2-9]|[1-8]\\d|9\\d?)\\d{3,10}|9(?:0[6-9]\\d{3,10}|1\\d{4,12}|[2-9]\\d{4,11})', example_number='30123456', possible_length=(5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), possible_length_local_only=(3, 4)),
    mobile=PhoneNumberDesc(national_number_pattern='1(?:5[0-25-9]\\d{8}|6[023]\\d{7,8}|7\\d{8,9})', example_number='15123456789', possible_length=(10, 11)),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7,12}', example_number='8001234567890', possible_length=(10, 11, 12, 13, 14, 15)),
    premium_rate=PhoneNumberDesc(national_number_pattern='137[7-9]\\d{6}|900(?:[135]\\d{6}|9\\d{7})', example_number='9001234567', possible_length=(10, 11)),
    shared_cost=PhoneNumberDesc(national_number_pattern='1(?:3(?:7[1-6]\\d{6}|8\\d{4})|80\\d{5,11})', example_number='18012345', possible_length=(7, 8, 9, 10, 11, 12, 13, 14)),
    personal_number=PhoneNumberDesc(national_number_pattern='700\\d{8}', example_number='70012345678', possible_length=(11,)),
    pager=PhoneNumberDesc(national_number_pattern='16(?:4\\d{1,10}|[89]\\d{1,11})', example_number='16412345', possible_length=(4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)),
    uan=PhoneNumberDesc(national_number_pattern='18(?:1\\d{5,11}|[2-9]\\d{8})', example_number='18500123456', possible_length=(8, 9, 10, 11, 12, 13, 14)),
    voicemail=PhoneNumberDesc(national_number_pattern='1(?:5(?:(?:2\\d55|7\\d99|9\\d33)\\d{7}|(?:[034568]00|113)\\d{8})|6(?:013|255|399)\\d{7,8}|7(?:[015]13|[234]55|[69]33|[78]99)\\d{7,8})', example_number='177991234567', possible_length=(12, 13)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(1\\d{2})(\\d{7,8})', format='\\1 \\2', leading_digits_pattern=['1[67]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(15\\d{3})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['15[0568]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1\\d{3})(\\d{7})', format='\\1 \\2', leading_digits_pattern=['15'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3,11})', format='\\1 \\2', leading_digits_pattern=['3[02]|40|[68]9'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3,11})', format='\\1 \\2', leading_digits_pattern=['2(?:0[1-389]|1[124]|2[18]|3[14]|[4-9]1)|3(?:[35-9][15]|4[015])|[4-8][1-9]1|9(?:06|[1-9]1)', '2(?:0[1-389]|1(?:[14]|2[0-8])|2[18]|3[14]|[4-9]1)|3(?:[35-9][15]|4[015])|[4-8][1-9]1|9(?:06|[1-9]1)'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{2,11})', format='\\1 \\2', leading_digits_pattern=['[24-6]|3(?:[3569][02-46-9]|4[2-4679]|7[2-467]|8[2-46-8])|[7-9](?:0[1-9]|[1-9])', '[24-6]|3(?:3(?:0[1-467]|2[127-9]|3[124578]|[46][1246]|7[1257-9]|8[1256]|9[145])|4(?:2[135]|3[1357]|4[13578]|6[1246]|7[1356]|9[1346])|5(?:0[14]|2[1-3589]|3[1357]|[49][1246]|6[1-4]|7[13468]|8[13568])|6(?:0[1356]|2[1-489]|3[124-6]|4[1347]|6[13]|7[12579]|8[1-356]|9[135])|7(?:2[1-7]|3[1357]|4[145]|6[1-5]|7[1-4])|8(?:21|3[1468]|4[1347]|6[0135-9]|7[1467]|8[136])|9(?:0[12479]|2[1358]|3[1357]|4[134679]|6[1-9]|7[136]|8[147]|9[1468]))|[7-9](?:0[1-9]|[1-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(3\\d{4})(\\d{1,10})', format='\\1 \\2', leading_digits_pattern=['3'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(800)(\\d{7,12})', format='\\1 \\2', leading_digits_pattern=['800'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d)(\\d{4,10})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:37|80)|900', '1(?:37|80)|900[1359]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1\\d{2})(\\d{5,11})', format='\\1 \\2', leading_digits_pattern=['181'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(18\\d{3})(\\d{6})', format='\\1 \\2', leading_digits_pattern=['185', '1850', '18500'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(18\\d{2})(\\d{7})', format='\\1 \\2', leading_digits_pattern=['18[68]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(18\\d)(\\d{8})', format='\\1 \\2', leading_digits_pattern=['18[2-579]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(700)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['700'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(138)(\\d{4})', format='\\1 \\2', leading_digits_pattern=['138'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(15[013-68])(\\d{2})(\\d{8})', format='\\1 \\2 \\3', leading_digits_pattern=['15[013-68]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(15[279]\\d)(\\d{2})(\\d{7})', format='\\1 \\2 \\3', leading_digits_pattern=['15[279]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1[67]\\d)(\\d{2})(\\d{7,8})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:6[023]|7)'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)