from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

bosh_menyu =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text="🎫 Online chipta buyurtma berish"), 
		],
		[
		KeyboardButton(text="📞 Kontaktlarimiz"),
		KeyboardButton(text="📲 Ijtimoiy tarmoqlardagi manzilimiz")
		],	
	],
	resize_keyboard=True
)
#Buyurtma turlari
buyurtma =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='✈️  🇺🇿 📍  Mahalliy parvoz'),
		KeyboardButton(text='✈️  🌐 📍  Xalqaro parvoz')
		],
		[
		KeyboardButton(text='Asosiy menyuga    ⏏️')
		],
	],
	resize_keyboard=True
)
#Mahalliy parvozga buyurtma berish
mahalliy =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text="✈   Toshkent-Samarqand   🇺🇿", callback_data='tosh')
		],
		[
		InlineKeyboardButton(text="✈      Farg'ona-Urganch       🇺🇿", callback_data='far')
		],
		[
		InlineKeyboardButton(text="✈      Qarshi-Namangan      🇺🇿", callback_data='qar')
		],
		[
		InlineKeyboardButton(text="Ortga    ⤴️", callback_data='ort_buyurtma')
		],
	],
)

#Toshkent - Samarqand yo'nalishga safar
tarif_tosh =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='💸 🛩 Biznes', callback_data='vaqt_biz_tosh'),
		InlineKeyboardButton(text='🪙 💰 Ekonom', callback_data='vaqt_eko_tosh'),
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data='ort_mahalliy')
		],

	],
)

#Toshkent - Samarqand tariflari (biznes)
tosh_vaqt_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='☀️   Kunduzgi',callback_data='tosh_biz_nat_kun'),
		InlineKeyboardButton(text='🌙   Kechki', callback_data='tosh_biz_nat_kech')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_tosh_mahalliy_tarif')
		],
	],
)

tosh_biz_nat_kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='tosh_biz_nat_kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_mahalliy_kun_qismi')
		],
	],
)

tosh_biz_nat_kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='tosh_biz_nat_kun')
		],
	],
)

tel =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text="📞  Telefon raqam jo'natish", request_contact=True)
		],
	],
	resize_keyboard=True
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

tosh_biz_nat_kech_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='tosh_biz_nat_kech_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_mahalliy_kun_qismi')
		],
	],
)

tosh_biz_nat_kech_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='tosh_biz_nat_kech')
		],
	],
)



#Toshkent - Samarqand tariflari (ekonom /kunduzgi)

tosh_vaqt_eko =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='☀️   Kunduzgi',callback_data='tosh_eko_nat_kun'),
		InlineKeyboardButton(text='🌙   Kechki', callback_data='tosh_eko_nat_kech')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_tosh_mahalliy_tarif')
		],
	],
)

tosh_eko_nat_kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='tosh_eko_nat_kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='vaqt_eko_tosh')
		],
	],
)

tosh_eko_nat_kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='tosh_eko_nat_kun')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#Toshkent - Samarqand tariflari (ekonom /kechgi)
tosh_eko_nat_kech_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='tosh_eko_nat_kech_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='vaqt_eko_tosh')
		],
	],
)

tosh_eko_nat_kech_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='tosh_eko_nat_kech')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)


#Farg'ona - Urganch yo'nalishga safar
tarif_far =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='💸 🛩 Biznes', callback_data='vaqt_biz_far'),
		InlineKeyboardButton(text='🪙 💰 Ekonom', callback_data='vaqt_eko_far'),
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data='ort_mahalliy')
		],

	],
)

#Farg'ona - Urganch tariflari (biznes)
far_vaqt_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='☀️   Kunduzgi',callback_data='far_biz_nat_kun'),
		InlineKeyboardButton(text='🌙   Kechki', callback_data='far_biz_nat_kech')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_far_mahalliy_tarif')
		],
	],
)

far_biz_nat_kun_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='far_biz_nat_kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_far_mahalliy_kun_qismi')
		],
	],
)

far_biz_nat_kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='far_biz_nat_kun')
		],
	],
)

far_biz_nat_kech_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='far_biz_nat_kech_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_far_mahalliy_kun_qismi')
		],
	],
)

far_biz_nat_kech_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='far_biz_nat_kech')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#Farg'ona - Urganch tariflari (ekonom)
far_vaqt_eko =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='☀️   Kunduzgi',callback_data='far_eko_nat_kun'),
		InlineKeyboardButton(text='🌙   Kechki', callback_data='far_eko_nat_kech')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_far_mahalliy_tarif')
		],
	],
)

#kunduzgi tariflar uchun
far_eko_kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='far_eko_nat_kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_far_eko_mahalliy_kun_qismi')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

far_eko_nat_kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='far_eko_nat_kun')
		],
	],
)

far_eko_kech_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='far_eko_nat_kech_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_far_eko_mahalliy_kun_qismi')
		],
	],
)

far_eko_nat_kech_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='far_eko_nat_kech')
		],
	],
)


#                             Qarshi - Namangan tariflari (biznes)
tarif_qar =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='💸 🛩 Biznes', callback_data='vaqt_biz_qar'),
		InlineKeyboardButton(text='🪙 💰 Ekonom', callback_data='vaqt_eko_qar'),
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data='ort_mahalliy')
		],

	],
)

qar_vaqt_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='☀️   Kunduzgi',callback_data='qar_biz_nat_kun'),
		InlineKeyboardButton(text='🌙   Kechki', callback_data='qar_biz_nat_kech')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_qar_mahalliy_tarif')
		],
	],
)

qar_biz_nat_kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='qar_biz_nat_kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='vaqt_biz_qar')
		],
	],
)

qar_biz_nat_kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='qar_biz_nat_kun')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

qar_biz_nat_kech_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='qar_biz_nat_kech_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='vaqt_biz_qar')
		],
	],
)

qar_biz_nat_kech_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='qar_biz_nat_kech')
		],
	],
)



#Qarshi - Namangan tariflari (ekonom /kunduzgi)

qar_vaqt_eko =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='☀️   Kunduzgi',callback_data='qar_eko_nat_kun'),
		InlineKeyboardButton(text='🌙   Kechki', callback_data='qar_eko_nat_kech')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_qar_mahalliy_tarif')
		],
	],
)

qar_eko_nat_kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='qar_eko_nat_kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='vaqt_eko_qar')
		],
	],
)

qar_eko_nat_kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='qar_eko_nat_kun')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#Qarshi - Namangan tariflari (ekonom /kunduzgi)

qar_eko_nat_kech_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='qar_eko_nat_kech_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='vaqt_eko_qar')
		],
	],
)

qar_eko_nat_kech_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='qar_eko_nat_kech')
		],
	],
)








#Xalqaro parvozga buyurtma berish
xalqaro =InlineKeyboardMarkup(
	inline_keyboard=[

		[
		InlineKeyboardButton(text="Olmaota,  (ALA).  Qozog'iston  ✈  🇰🇿", callback_data='kz')
		],
		[
		InlineKeyboardButton(text="Frankfurt,  (FRA).  Germaniya  ✈  🇩🇪", callback_data='ger')
		],
		[
		InlineKeyboardButton(text="Istanbul,  (IST).  Turkiya  ✈  🇹🇷", callback_data='ist')
		],
		[
		InlineKeyboardButton(text="Rim,  (FCO).  Italiya  ✈  🇮🇹", callback_data='rim')
		], 
		[
		InlineKeyboardButton(text="Dubay,  (DXB).  BAA  ✈  🇦🇪", callback_data='baa')
		],
		[
		InlineKeyboardButton(text="London,  (LHR).  BB  ✈  🇬🇧", callback_data='lon')
		],
		[
		InlineKeyboardButton(text="Ortga    ⤴️", callback_data='ort_buyurtma')
		],
	],
)

#Toshkent - Qozog'iston yo'nalishga safar
tarif_kz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='💸 🛩 Biznes', callback_data='vaqt_biz_kz'),
		InlineKeyboardButton(text='🪙 💰 Ekonom', callback_data='vaqt_eko_kz'),
		],
		[InlineKeyboardButton(text='💵 💰 Ekonom+', callback_data='vaqt_eko_plus_kz')
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data="ort_xalqaro")
		],

	],
)

#Toshkent - Qozog'iston tariflari (biznes)
kz_vaqt_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='kz_biz_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='kz_biz_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='kz_biz_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_xalqaro_tarif')
		],
	],
)

#3 kunlik tarif biznes
kz_biz_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_biz_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_xalqaro_3kun')
		],
	],
)

kz_biz_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='kz_biz_nat_3')
		],
	],
)

#5kunlik tarif biznes
kz_biz_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_biz_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_xalqaro_5kun')
		],
	],
)

kz_biz_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='kz_biz_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif biznes
kz_biz_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_biz_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_xalqaro_7kun')
		],
	],
)

kz_biz_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='kz_biz_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)



#Toshkent - Qozog'iston tariflari (ekonom)
kz_vaqt_eko =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='kz_eko_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='kz_eko_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='kz_eko_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_xalqaro_tarif')
		],
	],
)

#3 kunlik tarif ekonom
kz_eko_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_eko_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_eko_3kun')
		],
	],
)

kz_eko_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='kz_eko_nat_3')
		],
	],
)

#5kunlik tarif biznes
kz_eko_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_eko_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_eko_5kun')
		],
	],
)

kz_eko_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='kz_eko_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom
kz_eko_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_eko_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_eko_7kun')
		],
	],
)

kz_eko_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='kz_eko_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)


#Toshkent - Qozog'iston tariflari (ekonom +)
kz_vaqt_eko_plus =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='kz_eko_plus_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='kz_eko_plus_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='kz_eko_plus_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_xalqaro_tarif')
		],
	],
)

#3 kunlik tarif ekonom
kz_eko_plus_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_eko_plus_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_eko_plus_3kun')
		],
	],
)

kz_eko_plus_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='kz_eko_plus_nat_3')
		],
	],
)

#5kunlik tarif biznes
kz_eko_plus_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_eko_plus_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_eko_plus_5kun')
		],
	],
)

kz_eko_plus_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='kz_eko_plus_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom +
kz_eko_plus_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='kz_eko_plus_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_kz_eko_plus_7kun')
		],
	],
)

kz_eko_plus_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='kz_eko_plus_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)













#Toshkent - Frankfurt yo'nalishga safar
tarif_ger =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='💸 🛩 Biznes', callback_data='vaqt_biz_ger'),
		InlineKeyboardButton(text='🪙 💰 Ekonom', callback_data='vaqt_eko_ger'),
		],
		[InlineKeyboardButton(text='💵 💰 Ekonom+', callback_data='vaqt_eko_plus_ger')
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data="ort_xalqaro")
		],

	],
)

#Toshkent - Frankfurt tariflari (biznes)
ger_vaqt_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='ger_biz_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='ger_biz_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='ger_biz_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_xalqaro_tarif')
		],
	],
)

#3 kunlik tarif biznes
ger_biz_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_biz_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_xalqaro_3kun')
		],
	],
)

ger_biz_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='ger_biz_nat_3')
		],
	],
)

#5kunlik tarif biznes
ger_biz_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_biz_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_xalqaro_5kun')
		],
	],
)

ger_biz_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ger_biz_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif biznes
ger_biz_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_biz_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_xalqaro_7kun')
		],
	],
)

ger_biz_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ger_biz_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)



#Toshkent - Frankfurt tariflari (ekonom)
ger_vaqt_eko =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='ger_eko_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='ger_eko_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='ger_eko_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_xalqaro_tarif')
		],
	],
)

#3 kunlik tarif ekonom
ger_eko_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_eko_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_eko_3kun')
		],
	],
)

ger_eko_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='ger_eko_nat_3')
		],
	],
)

#5kunlik tarif ekonom
ger_eko_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_eko_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_eko_5kun')
		],
	],
)

ger_eko_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ger_eko_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom
ger_eko_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_eko_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_eko_7kun')
		],
	],
)

ger_eko_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ger_eko_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)


#Toshkent - Frankfurt tariflari (ekonom +)
ger_vaqt_eko_plus =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='ger_eko_plus_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='ger_eko_plus_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='ger_eko_plus_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_xalqaro_tarif')
		],
	],
)

#3 kunlik tarif ekonom +
ger_eko_plus_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_eko_plus_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_eko_plus_3kun')
		],
	],
)

ger_eko_plus_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='ger_eko_plus_nat_3')
		],
	],
)

#5kunlik tarif ekonom +
ger_eko_plus_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_eko_plus_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_eko_plus_5kun')
		],
	],
)

ger_eko_plus_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ger_eko_plus_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom +
ger_eko_plus_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ger_eko_plus_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ger_eko_plus_7kun')
		],
	],
)

ger_eko_plus_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ger_eko_plus_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)









#Toshkent - Istanbul yo'nalishga safar
tarif_ist =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='💸 🛩 Biznes', callback_data='vaqt_biz_ist'),
		InlineKeyboardButton(text='🪙 💰 Ekonom', callback_data='vaqt_eko_ist'),
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data="ort_xalqaro")
		],

	],
)

#Toshkent - Istanbul tariflari (biznes)
ist_vaqt_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='ist_biz_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='ist_biz_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='ist_biz_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ist_xalqaro_tarif')
		],
	],
)

#3 kunlik tarif biznes
ist_biz_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ist_biz_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ist_xalqaro_3kun')
		],
	],
)

ist_biz_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='ist_biz_nat_3')
		],
	],
)

#5kunlik tarif biznes
ist_biz_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ist_biz_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ist_xalqaro_5kun')
		],
	],
)

ist_biz_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ist_biz_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif biznes
ist_biz_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ist_biz_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ist_xalqaro_7kun')
		],
	],
)

ist_biz_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ist_biz_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)



#Toshkent - Istanbul tariflari (ekonom)
ist_vaqt_eko =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='ist_eko_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='ist_eko_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='ist_eko_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ist_xalqaro_tarif')
		],
	],
)

#3 kunlik tarif ekonom
ist_eko_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ist_eko_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ist_eko_3kun')
		],
	],
)

ist_eko_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='ist_eko_nat_3')
		],
	],
)

#5kunlik tarif ekonom
ist_eko_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ist_eko_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ist_eko_5kun')
		],
	],
)

ist_eko_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ist_eko_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom
ist_eko_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='ist_eko_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_ist_eko_7kun')
		],
	],
)

ist_eko_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='ist_eko_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)













#Toshkent - Rim yo'nalishga safar
tarif_rim =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='🪙 💰 Ekonom', callback_data='vaqt_eko_rim'),
		InlineKeyboardButton(text='💵 💰 Ekonom+', callback_data='vaqt_eko_plus_rim')
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data="ort_xalqaro")
		],

	],
)

#Toshkent - Rim tariflari (ekonom)
rim_vaqt_eko =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='rim_eko_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='rim_eko_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='rim_eko_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_rim_eko_tarif')
		],
	],
)

#3 kunlik tarif ekonom
rim_eko_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='rim_eko_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_rim_eko_3kun')
		],
	],
)

rim_eko_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='rim_eko_nat_3')
		],
	],
)

#5kunlik tarif ekonom
rim_eko_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='rim_eko_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_rim_eko_5kun')
		],
	],
)

rim_eko_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='rim_eko_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom
rim_eko_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='rim_eko_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_rim_eko_7kun')
		],
	],
)

rim_eko_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='rim_eko_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)


#Toshkent - Rim tariflari (ekonom +)
rim_vaqt_eko_plus =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='rim_eko_plus_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='rim_eko_plus_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='rim_eko_plus_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_rim_eko_tarif')
		],
	],
)

#3 kunlik tarif ekonom +
rim_eko_plus_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='rim_eko_plus_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_rim_eko_plus_3kun')
		],
	],
)

rim_eko_plus_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='rim_eko_plus_nat_3')
		],
	],
)

#5kunlik tarif ekonom +
rim_eko_plus_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='rim_eko_plus_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_rim_eko_plus_5kun')
		],
	],
)

rim_eko_plus_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='rim_eko_plus_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom +
rim_eko_plus_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='rim_eko_plus_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_rim_eko_plus_7kun')
		],
	],
)

rim_eko_plus_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='rim_eko_plus_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)





#Toshkent - Dubay yo'nalishga safar
tarif_baa =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='💸 🛩 Biznes', callback_data='vaqt_biz_baa'),
		InlineKeyboardButton(text='💵 💰 Ekonom+', callback_data='vaqt_eko_plus_baa'),
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data="ort_xalqaro")
		],

	],
)

#Toshkent - Dubay tariflari (biznes)
baa_vaqt_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='baa_biz_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='baa_biz_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='baa_biz_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_baa_tarif')
		],
	],
)

#3 kunlik tarif biznes
baa_biz_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='baa_biz_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_baa_xalqaro_3kun')
		],
	],
)

baa_biz_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='baa_biz_nat_3')
		],
	],
)

#5kunlik tarif biznes
baa_biz_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='baa_biz_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_baa_xalqaro_5kun')
		],
	],
)

baa_biz_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='baa_biz_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif biznes
baa_biz_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='baa_biz_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_baa_xalqaro_7kun')
		],
	],
)

baa_biz_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='baa_biz_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#Toshkent - Dubay tariflari (ekonom +)
baa_vaqt_eko_plus =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='baa_eko_plus_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='baa_eko_plus_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='baa_eko_plus_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_baa_tarif')
		],
	],
)

#3 kunlik tarif ekonom +
baa_eko_plus_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='baa_eko_plus_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_baa_eko_plus_3kun')
		],
	],
)

baa_eko_plus_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='baa_eko_plus_nat_3')
		],
	],
)

#5kunlik tarif ekonom +
baa_eko_plus_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='baa_eko_plus_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_baa_eko_plus_5kun')
		],
	],
)

baa_eko_plus_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='baa_eko_plus_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom +
baa_eko_plus_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='baa_eko_plus_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_baa_eko_plus_7kun')
		],
	],
)

baa_eko_plus_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='baa_eko_plus_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)






#Toshkent - London yo'nalishga safar
tarif_bb =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='💸 🛩 Biznes', callback_data='vaqt_biz_bb'),
		InlineKeyboardButton(text='💵 💰 Ekonom+', callback_data='vaqt_eko_plus_bb'),
		],
		[
		InlineKeyboardButton(text='Ortga   ⤴️', callback_data="ort_xalqaro")
		],

	],
)

#Toshkent - London tariflari (biznes)
bb_vaqt_biz =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='bb_biz_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='bb_biz_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='bb_biz_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_bb_tarif')
		],
	],
)

#3 kunlik tarif biznes
bb_biz_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='bb_biz_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_bb_xalqaro_3kun')
		],
	],
)

bb_biz_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='bb_biz_nat_3')
		],
	],
)

#5kunlik tarif biznes
bb_biz_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='bb_biz_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_bb_xalqaro_5kun')
		],
	],
)

bb_biz_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='bb_biz_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif biznes
bb_biz_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='bb_biz_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_bb_xalqaro_7kun')
		],
	],
)

bb_biz_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='bb_biz_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#Toshkent - Dubay tariflari (ekonom +)
bb_vaqt_eko_plus =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='3 kun ichida',callback_data='bb_eko_plus_nat_3')
		],
		[
		InlineKeyboardButton(text='5 kun ichida', callback_data='bb_eko_plus_nat_5')
		],
		[
		InlineKeyboardButton(text='bir hafta ichida', callback_data='bb_eko_plus_nat_7')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_bb_tarif')
		],
	],
)

#3 kunlik tarif ekonom +
bb_eko_plus_nat_3kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='bb_eko_plus_nat_3kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_bb_eko_plus_3kun')
		],
	],
)

bb_eko_plus_nat_3kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman  ✅', callback_data='bb_eko_plus_nat_3')
		],
	],
)

#5kunlik tarif ekonom +
bb_eko_plus_nat_5kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='bb_eko_plus_nat_5kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_bb_eko_plus_5kun')
		],
	],
)

bb_eko_plus_nat_5kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='bb_eko_plus_nat_5')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)

#7kunlik tarif ekonom +
bb_eko_plus_nat_7kun_knopka =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Buyurtma berish', callback_data='tugat')
		],
		[
		InlineKeyboardButton(text='Jarimalar', callback_data='bb_eko_plus_nat_7kun_jarima')
		],
		[
		InlineKeyboardButton(text='Ortga     ⤴️', callback_data='ort_bb_eko_plus_7kun')
		],
	],
)

bb_eko_plus_nat_7kun_roziman =InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(text='Roziman   ✅', callback_data='bb_eko_plus_nat_7')
		],
	],
)

qayta =ReplyKeyboardMarkup(
	keyboard=[
		[
		KeyboardButton(text='🔄  Qayta harid qilish')
		],
	],
	resize_keyboard=True
)