import logging
from config import API_TOKEN 
from buttons import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery

from class_file import Info 
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
x =Info()
ADMIN = INT("ADMIN'S ID HERE")


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \n✈ 🗺  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz 🤵‍♂🤵‍♀",reply_markup=bosh_menyu)
    x.create_table()

#Kontakt va ijtimoiy tarmoq haqida malumot beruvchi tag tugmalar

@dp.message_handler(text="📞 Kontaktlarimiz")
async def kontakt(message: types.Message):
	await message.answer("<b>Kontaktlar</b> \n\n<b>Aloqa markazi</b>\n+998781400200\n<ins>kecha-kunduz</ins>\
		\n\n<b>Ishonch telefoni</b>\n+998781204770\n<ins>Har kuni: 9:00 - 18:00 gacha</ins>", parse_mode='HTML')

@dp.message_handler(text="📲 Ijtimoiy tarmoqlardagi manzilimiz")
async def ijtimoiy(message: types.Message):
	await message.answer("<b>Uzbekistan Airways ijtimoiy tarmoqlarda</b>\
		\n\n<ins>Instagram:</ins> \
		https://www.instagram.com/uzairways/ \
		\n\n<ins>Telegram:</ins> https://t.me/uzbekistanairways \
		\n\n<ins>Facebook:</ins> https://www.facebook.com/\
		uzairways.official/\
		\n\n<ins>You Tube:</ins> https://www.youtube.com/c/UzbekistanAirwaysHY \
		\n\n<ins>Linked in:</ins> https://www.linkedin.com/company/uzbekistan-airways-jsc", parse_mode='HTML')

@dp.message_handler(text="Asosiy menyuga    ⏏️")
async def ortga(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \n✈ 🗺  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz 🤵‍♂🤵‍♀",reply_markup=bosh_menyu)
	
#Buyurtma berish qismi

@dp.message_handler(text="🎫 Online chipta buyurtma berish")
async def chipta(message: types.Message):
	await message.answer("Parvoz turini tanlang  [Mahalliy/ Xalqaro]  🔽",reply_markup=buyurtma)

#Mahalliy parvozga buyurtma berish

@dp.message_handler(text="✈️  🇺🇿 📍  Mahalliy parvoz")
async def mahaliy(message: types.Message):
	await message.answer("Quyidagi shaharlarga parvozlar mavjud", reply_markup=mahalliy)

#Mahalliy tariflar vaqtlari Toshkent - Samarqand 
@dp.callback_query_handler(text="ort_buyurtma")
async def tosh_sam(call:CallbackQuery):
	await call.message.answer("Parvoz turini tanlang  [Mahalliy/ Xalqaro]  🔽",reply_markup=buyurtma)

@dp.callback_query_handler(text="tosh")
async def tosh_sam(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_tosh)

@dp.callback_query_handler(text="ort_mahalliy")
async def tosh_sam(call:CallbackQuery):
	await call.message.answer("Quyidagi shaharlarga parvozlar mavjud", reply_markup=mahalliy)

#biznes klass uchun 
@dp.callback_query_handler(text="vaqt_biz_tosh")
async def tosh_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=tosh_vaqt_biz)

@dp.callback_query_handler(text="ort_tosh_mahalliy_tarif")
async def mahalliy_tosh_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_tosh)

#kunduzgi tarif
@dp.callback_query_handler(text="tosh_biz_nat_kun")
async def tosh_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Samarqand\
		\n🛫  Uchib Ketish vaqti  --  11:20  /  \n🛬 Qo'nish vaqti  --  12:30\
		\n\n🧳❗️  Qo'l yuki uchun qo'yilgan talablar  🔽\nMaksimal vazni: 18kg / \nMaksimal hajmi: 180sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 1000 ball\
		\nChipta narxi - 720 500 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=tosh_biz_nat_kun_knopka)

@dp.callback_query_handler(text="tosh_biz_nat_kun_jarima")
async def tosh_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  36 550  UZS\nParvozdan keyin: 38 379 UZS\
		\n\n🔙  Avaichiptani qaytarish  45 770  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=tosh_biz_nat_kun_roziman)

@dp.callback_query_handler(text="ort_mahalliy_kun_qismi")
async def tosh_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=tosh_vaqt_biz)


#kechki tarif
@dp.callback_query_handler(text="tosh_biz_nat_kech")
async def tosh_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Samarqand\
		\n🛫  Uchib Ketish vaqti  --  19:20  /  \n🛬 Qo'nish vaqti  --  20:30\
		\n\n🧳❗️  Qo'l yuki uchun qo'yilgan talablar  🔽\nMaksimal vazni: 18kg / \nMaksimal hajmi: 180sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 1000 ball\
		\nChipta narxi - 720 500 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=tosh_biz_nat_kech_knopka)

@dp.callback_query_handler(text="tugat")
async def tosh_kun_tugat(call:CallbackQuery):
	await call.message.reply("<ins>🎉  Tabriklaymiz!!!</ins>\
	\n<b>Siz [Uzbekistan Airways] ning \nSovrinli aviachipta o'yini ishtirokchisiga aylandigiz</b> ❗️❗️❗️, \
	\n\nQuyida telefon raqamingizni qoldiring...",\
	parse_mode='HTML',reply_markup=tel)

@dp.message_handler(content_types=['contact'], is_sender_contact=True)
async def contact_handler(message: types.Message):
	user_id =message.from_user.id
	username =message.from_user.username
	firstname =message.from_user.full_name
	raqam =message.contact['phone_number']
	user_check =x.check(user_id)
	if user_check is None:
		x.insert(user_id, username, firstname)
		x.update_num(user_id, raqam)
		z =x.user_entry_info(user_id)
		await bot.send_message(ADMIN,f"Foydalanuvchi ro'yhatdan o'tdi.\
		\nId: {z[0]} \nTo'liq ismi: {z[2]} \nUsername: @{z[1]} \nTel raqam: {z[3]}")
		
		await message.answer("✅  Sizning ma'lumotlaringiz qabul qilib olindi\
			\n\nHaridingiz uchun rahmat !! \nCall center bo'limi siz bilan tez orada bog'lanadi...📞", \
			reply_markup=qayta)
	else:
		await message.answer("✅  Sizning ma'lumotlaringiz qabul qilib olindi\
			\n\nHaridingiz uchun rahmat !! \nCall center bo'limi siz bilan tez orada bog'lanadi...📞", \
			reply_markup=qayta)
        
#Ro'yhatdan o'tgan foydalanuvchilar username va id sini tartibli holatida qaytaradi
@dp.message_handler(commands='Alluser', user_id=ADMIN)
async def allusers(message: types.Message):
	user_id =message.from_user.id
	counted =x.user_counter(user_id)
	users =x.users_id()
	son =0
	userlist =""
	for user in users:
		son +=1
		userlist +=f"\n {son}) Id: {user[0]} \nUsername: @{user[1]}" 
		
	await bot.send_message(ADMIN, f"Foydalanuvchilar soni: {counted[0][0]} ta \
		\n{userlist}")
#Ro'yhatdan o'tgan foydalanuvchilar username va id sini list holatida qaytaradi
@dp.message_handler(commands='all', user_id=ADMIN)
async def userss(message: types.Message):
    user_id =message.from_user.id
    user =x.users(user_id)
    await bot.send_message(ADMIN,user)
    
@dp.callback_query_handler(text="tosh_biz_nat_kech_jarima")
async def tosh_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  36 550  UZS\nParvozdan keyin: 38 379 UZS\
		\n\n🔙  Avaichiptani qaytarish  45 770  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=tosh_biz_nat_kech_roziman)

@dp.message_handler(text='🔄  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \n✈ 🗺  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz 🤵‍♂🤵‍♀",reply_markup=bosh_menyu)



#ekonom klass uchun (kunduzgi)
@dp.callback_query_handler(text="vaqt_eko_tosh")
async def tosh_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=tosh_vaqt_eko)

#kunduzgi tarif 
@dp.callback_query_handler(text="tosh_eko_nat_kun")
async def tosh_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Samarqand\
		\n🛫  Uchib Ketish vaqti  --  09:00  /  \n🛬 Qo'nish vaqti  --  11:30\
		\n\n🧳❗❌️  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ❌\
		\n\nUzairplus - 800 ball\
		\nChipta narxi - 637 606 UZS,\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=tosh_eko_nat_kun_knopka)

@dp.message_handler(content_types=['contact'])
async def contact_handler(message: types.Message):
	raqam =message.contact['phone_number']
	db.update_num(userid, raqam)
	z =x.user_entry_info(user_id)
	await bot.send_message(ADMIN,f"Foydalanuvchi ro'yhatdan o'tdi.\
	\nId: {z[0]} \nIsmi: {z[2]} \nUsername: @{z[1]} \nTel raqam: {z[3]}" )

@dp.callback_query_handler(text="tosh_eko_nat_kun_jarima")
async def tosh_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  36 550  UZS\nParvozdan keyin: 38 379 UZS\
		\n\n🔙  Avaichiptani qaytarish  45 770  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=tosh_eko_nat_kun_roziman)

#kechki tarif
@dp.callback_query_handler(text="tosh_eko_nat_kech")
async def tosh_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Samarqand\
		\n🛫  Uchib Ketish vaqti  --  21:00  /  \n🛬 Qo'nish vaqti  --  22:30\
		\n\n🧳❗❌️  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ❌\
		\n\nUzairplus - 800 ball\
		\nChipta narxi - 637 606 UZS,\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=tosh_eko_nat_kech_knopka)

@dp.callback_query_handler(text="tosh_eko_nat_kech_jarima")
async def tosh_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  27 500  UZS\nParvozdan keyin: 35 380 UZS\
		\n\n🔙  Avaichiptani qaytarish:  Parvozdan keyin tarif shuningdek, YQ, YQ yig‘imlari to'liq ushlab qolinadi. Aeroport yig‘mlari va boshqa to‘lovlar qaytariladi.\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=tosh_eko_nat_kech_roziman)

@dp.message_handler(text='🔄  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \n✈ 🗺  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz 🤵‍♂🤵‍♀",reply_markup=bosh_menyu)


#Mahalliy tariflar vaqtlari Farg'ona - Urganch
@dp.callback_query_handler(text="far")
async def far_urg(call:CallbackQuery):
	await call.message.reply("Tarifni tanlang", reply_markup=tarif_far)

#biznes klass uchun 
@dp.callback_query_handler(text="vaqt_biz_far")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=far_vaqt_biz)

@dp.callback_query_handler(text="ort_far_mahalliy_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_far)


#kunduzgi tarif
@dp.callback_query_handler(text="far_biz_nat_kun")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'alish:  Farg'ona - Urganch\
		\n🛫  Uchib Ketish vaqti  --  12:20  /  \n🛬 Qo'nish vaqti  --  14:10\
		\n\n🧳❗️  Qo'l yuki uchun qo'yilgan talablar  🔽\nMaksimal vazni: 16kg / \nMaksimal hajmi: 140sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 1200 ball\
		\nChipta narxi - 890 384 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=far_biz_nat_kun_biz)

@dp.callback_query_handler(text="far_biz_nat_kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  122 660  UZS\nParvozdan keyin: 143 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  165 770  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=far_biz_nat_kun_roziman)

@dp.callback_query_handler(text="ort_far_mahalliy_kun_qismi")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=far_vaqt_biz)

@dp.callback_query_handler(text="ort_far_eko_mahalliy_kun_qismi")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=far_vaqt_eko)

#kechki tarif
@dp.callback_query_handler(text="far_biz_nat_kech")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish: Farg'ona - Urganch\
		\n🛫  Uchib Ketish vaqti  --  20:25  /  \n🛬 Qo'nish vaqti  --  21:55\
		\n\n🧳❗️  Qo'l yuki uchun qo'yilgan talablar  🔽\nMaksimal vazni: 16kg / \nMaksimal hajmi: 140sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 1000 ball\
		\nChipta narxi - 879 550 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=far_biz_nat_kech_biz)

@dp.callback_query_handler(text="far_biz_nat_kech_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  122 660  UZS\nParvozdan keyin: 143 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  165 770  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=far_biz_nat_kech_roziman)


@dp.message_handler(text='🔄  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \n✈ 🗺  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz 🤵‍♂🤵‍♀",reply_markup=bosh_menyu)



#ekonom klass uchun (kunduzgi)
@dp.callback_query_handler(text="vaqt_eko_far")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=far_vaqt_eko)

#kunduzgi tarif 
@dp.callback_query_handler(text="far_eko_nat_kun")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Farg'ona - Urganch\
		\n🛫  Uchib Ketish vaqti  --  12:20  /  \n🛬 Qo'nish vaqti  --  14:10\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ❌\
		\n\nUzairplus - 900 ball\
		\nChipta narxi - 740 284 UZS,\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=far_eko_kun_knopka)

@dp.callback_query_handler(text="far_eko_nat_kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  122 660  UZS\nParvozdan keyin: 143 388 UZS\
		\n\n🔙  Avaichiptani qaytarish: \nRuxsat etilmaydi  ❌\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=far_eko_nat_kun_roziman)

#kechki tarif
@dp.callback_query_handler(text="far_eko_nat_kech")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Farg'ona - Urganch\
		\n🛫  Uchib Ketish vaqti  --  20:00  /  \n🛬 Qo'nish vaqti  --  21:20\
		\n\n🧳❗❌️  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ❌\
		\n\nUzairplus - 900 ball\
		\nChipta narxi - 740 284 UZS,\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=far_eko_kech_knopka)

@dp.callback_query_handler(text="far_eko_nat_kech_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  122 660  UZS\nParvozdan keyin: 143 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  \nRuxsat etilmaydi  ❌\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=far_eko_nat_kech_roziman)


@dp.message_handler(text='🔄  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \n✈ 🗺  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz 🤵‍♂🤵‍♀",reply_markup=bosh_menyu)


#Qarshi-Namangan
@dp.callback_query_handler(text="qar")
async def far_urg(call:CallbackQuery):
	await call.message.reply("Tarifni tanlang", reply_markup=tarif_qar)


#biznes klass uchun 
@dp.callback_query_handler(text="vaqt_biz_qar")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=qar_vaqt_biz)

@dp.callback_query_handler(text="ort_qar_mahalliy_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_qar)


#kunduzgi tarif
@dp.callback_query_handler(text="qar_biz_nat_kun")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Qarshi - Namangan\
		\n🛫  Uchib Ketish vaqti  --  10:30  /  \n🛬 Qo'nish vaqti  --  12:20\
		\n\n🧳❗️  Qo'l yuki uchun qo'yilgan talablar  🔽\nMaksimal vazni: 19kg / \nMaksimal hajmi: 200sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 900 ball\
		\nChipta narxi - 649 324 UZS\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=qar_biz_nat_kun_knopka)

@dp.callback_query_handler(text="qar_biz_nat_kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  35 639  UZS\nParvozdan keyin: 39 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  55 750  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=qar_biz_nat_kun_roziman)

@dp.callback_query_handler(text="ort_qar_mahalliy_kun_qismi")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=qar_vaqt_biz)

@dp.callback_query_handler(text="ort_qar_eko_mahalliy_kun_qismi")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=qar_vaqt_eko)

#kechki tarif
@dp.callback_query_handler(text="qar_biz_nat_kech")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish: Qarshi - Namangan\
		\n🛫  Uchib Ketish vaqti  --  19:25  /  \n🛬 Qo'nish vaqti  --  20:35\
		\n\n🧳❗️  Qo'l yuki uchun qo'yilgan talablar  🔽\nMaksimal vazni: 19kg / \nMaksimal hajmi: 200sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 900 ball\
		\nChipta narxi - 624 550 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=qar_biz_nat_kech_knopka)

@dp.callback_query_handler(text="qar_biz_nat_kech_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  35 639  UZS\nParvozdan keyin: 39 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  55 750  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=qar_biz_nat_kech_roziman)


@dp.message_handler(text='🔄  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \n✈ 🗺  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz 🤵‍♂🤵‍♀",reply_markup=bosh_menyu)



#ekonom klass uchun (kunduzgi)
@dp.callback_query_handler(text="vaqt_eko_qar")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=qar_vaqt_eko)

#kunduzgi tarif 
@dp.callback_query_handler(text="qar_eko_nat_kun")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Qarshi - Namangan\
		\n🛫  Uchib Ketish vaqti  --  12:00  /  \n🛬 Qo'nish vaqti  --  13:20\
		\n\n🧳❗❌️  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ❌\
		\n\nUzairplus - 600 ball\
		\nChipta narxi - 534 284 UZS\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=qar_eko_nat_kun_knopka)

@dp.callback_query_handler(text="qar_eko_nat_kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  25 300  UZS\nParvozdan keyin: 33 480 UZS\
		\n\n🔙  Avaichiptani qaytarish:  Parvozdan keyin tarif shuningdek, YQ, YQ yig‘imlari to'liq ushlab qolinadi. Aeroport yig‘mlari va boshqa to‘lovlar qaytariladi.\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=qar_eko_nat_kun_roziman)

#kechki tarif
@dp.callback_query_handler(text="qar_eko_nat_kech")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Qarshi - Namangan\
		\n🛫  Uchib Ketish vaqti  --  20:00  /  \n🛬 Qo'nish vaqti  --  21:20\
		\n\n🧳❗❌️  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ❌\
		\n\nUzairplus - 600 ball\
		\nChipta narxi - 554 300 UZS \nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=qar_eko_nat_kech_knopka)

@dp.callback_query_handler(text="qar_eko_nat_kech_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  📃  🖋  Aviachiptani qayta rasmiylashtirish  🔽\
		\nParvozdan oldin:  25 300  UZS\nParvozdan keyin: 33 480 UZS\
		\n\n🔙  Avaichiptani qaytarish:  Parvozdan keyin tarif shuningdek, YQ, YQ yig‘imlari to'liq ushlab qolinadi. Aeroport yig‘mlari va boshqa to‘lovlar qaytariladi.\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=qar_eko_nat_kech_roziman)


@dp.message_handler(text='🔄  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \n✈ 🗺  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz 🤵‍♂🤵‍♀",reply_markup=bosh_menyu)









#Xalqaro parvozga buyurtma berish
@dp.message_handler(text="✈️  🌐 📍  Xalqaro parvoz")
async def xaqaro(message: types.Message):
	await message.answer("Quyidagi davlatlarga parvozlar mavjud", reply_markup=xalqaro)

@dp.callback_query_handler(text="ort_buyurtma")
async def xaqaro(call:CallbackQuery):
	await call.message.answer("Parvoz turini tanlang  [Mahalliy/ Xalqaro]  🔽",reply_markup=buyurtma)

@dp.callback_query_handler(text="kz")
async def far_urg(call:CallbackQuery):
	await call.message.reply("Yonalish:  Toshkent-Olmaota  \nTarifni tanlang", reply_markup=tarif_kz)

#Toshkent - Qozog'iston yo'nalishga safar
#biznes klass uchun 
@dp.callback_query_handler(text="vaqt_biz_kz")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=kz_vaqt_biz)

@dp.callback_query_handler(text="ort_xalqaro")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Quyidagi davlatlarga parvozlar mavjud", reply_markup=xalqaro)


#3 kunlik tarif biznes
@dp.callback_query_handler(text="ort_kz_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_kz)

@dp.callback_query_handler(text="kz_biz_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  14:00  /  \n🛬 Qo'nish vaqti  --  16:30\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 1005 ball\
		\nChipta narxi - 7 312 307 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="kz_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  170 600  UZS\n▶  Parvozdan keyin: 185 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  245 320 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_kz_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_biz)

#5 kunlik tarif biznes
@dp.callback_query_handler(text="ort_kz_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_kz)

@dp.callback_query_handler(text="kz_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  15:50  /  \n🛬 Qo'nish vaqti  --  18:20\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 10kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 1000 ball\
		\nChipta narxi - 7 861 990\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="kz_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  171 400  UZS\n▶  Parvozdan keyin: 183 989 UZS\
		\n\n🔙  Avaichiptani qaytarish  264 320 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_kz_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_biz)

#7 kunlik tarif biznes
@dp.callback_query_handler(text="ort_kz_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_kz)

@dp.callback_query_handler(text="kz_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  14:00  /  \n🛬 Qo'nish vaqti  --  16:30\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 10kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 938 ball\
		\nChipta narxi - 6 037 341 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>bir hafta ichida</ins>",parse_mode='HTML', reply_markup=kz_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="kz_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS  UZS\n▶  Parvozdan keyin: 183 990 UZS UZS\
		\n\n🔙  Avaichiptani qaytarish  245 320 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_biz_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_kz_xalqaro_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_biz)

#ekonom klass uchun
@dp.callback_query_handler(text="vaqt_eko_kz")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=kz_vaqt_eko)


#3 kunlik tarif ekonom
@dp.callback_query_handler(text="ort_kz_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_kz)

@dp.callback_query_handler(text="kz_eko_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  14:00  /  \n🛬 Qo'nish vaqti  --  16:30\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 670 ball\
		\nChipta narxi - 4 762 375 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_nat_3kun_knopka)

@dp.callback_query_handler(text="kz_eko_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 135 990  UZS\
		\n\n🔙  Avaichiptani qaytarish 245 320 UZS UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko)

#5 kunlik tarif
@dp.callback_query_handler(text="kz_eko_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  07:30  /  \n🛬 Qo'nish vaqti  --  10:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 603 ball\
		\nChipta narxi - 3 087 419 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_nat_5kun_knopka)

@dp.callback_query_handler(text="kz_eko_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS  UZS\n▶  Parvozdan keyin: 136 800 UZS\
		\n\n🔙  Avaichiptani qaytarish  245 320 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko)

#7 kunlik tarif
@dp.callback_query_handler(text="kz_eko_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  14:00  /  \n🛬 Qo'nish vaqti  --  16:30\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 670 ball\
		\nChipta narxi - 3 824 900 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>bir hafta ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_nat_7kun_knopka)

@dp.callback_query_handler(text="kz_eko_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS  UZS\n▶  Parvozdan keyin: 183 990 UZS UZS\
		\n\n🔙  Avaichiptani qaytarish  245 320 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko)

#ekonom+ klass uchun
@dp.callback_query_handler(text="vaqt_eko_plus_kz")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=kz_vaqt_eko_plus)


#3 kunlik tarif ekonom plus

@dp.callback_query_handler(text="kz_eko_plus_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  12:00  /  \n🛬 Qo'nish vaqti  --  14:30\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 27kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 800 ball\
		\nChipta narxi - 5 862 370 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="kz_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 135 990  UZS\
		\n\n🔙  Avaichiptani qaytarish 245 320 UZS UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko_plus)

#5 kunlik tarif ekonom plus
@dp.callback_query_handler(text="kz_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  09:00  /  \n🛬 Qo'nish vaqti  --  12:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 27kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 805 ball\
		\nChipta narxi - 4 687 420 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="kz_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS  UZS\n▶  Parvozdan keyin: 136 800 UZS\
		\n\n🔙  Avaichiptani qaytarish  245 320 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko_plus)

#7 kunlik tarif
@dp.callback_query_handler(text="kz_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Qozog'iston\
		\n✈️  Samolyot modeli  --  Airbus  320\
		\n🛫  Uchib Ketish vaqti  --  14:00  /  \n🛬 Qo'nish vaqti  --  16:30\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 27kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 870 ball\
		\nChipta narxi - 4 850 900 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>bir hafta ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="kz_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS  UZS\n▶  Parvozdan keyin: 183 990 UZS UZS\
		\n\n🔙  Avaichiptani qaytarish  245 320 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_plus_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_plus_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko_plus)



@dp.callback_query_handler(text="ger")
async def far_urg(call:CallbackQuery):
	await call.message.reply("Tarifni tanlang", reply_markup=tarif_ger)


#Toshkent - Germaniya yo'nalishga safar
#biznes klass uchun 
@dp.callback_query_handler(text="vaqt_biz_ger")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=ger_vaqt_biz)

@dp.callback_query_handler(text="ort_xalqaro")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Quyidagi davlatlarga parvozlar mavjud", reply_markup=xalqaro)


#3 kunlik tarif biznes
@dp.callback_query_handler(text="ort_ger_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_ger)

@dp.callback_query_handler(text="ger_biz_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti  --  05:45  /  \n🛬 Qo'nish vaqti  --  09:40\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: P2-8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 7032 ball\
		\nChipta narxi - 19 047 340 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="ger_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  250 600  UZS\n▶  Parvozdan keyin: 279 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ger_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_biz)

#5 kunlik tarif biznes
@dp.callback_query_handler(text="ort_ger_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_ger)

@dp.callback_query_handler(text="ger_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti  --  05:45  /  \n🛬 Qo'nish vaqti  --  09:40\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: P2-8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 7032 ball\
		\nChipta narxi - 19 047 340 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="ger_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  250 600  UZS\n▶  Parvozdan keyin: 279 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ger_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_biz)

#7 kunlik tarif biznes
@dp.callback_query_handler(text="ort_ger_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_ger)

@dp.callback_query_handler(text="ger_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent -  Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  05:45  /  \n🛬 Qo'nish vaqti  --  09:40\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: P2-8kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 6563 ball\
		\nChipta narxi - 11 366 360 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>bir hafta ichida</ins>",parse_mode='HTML', reply_markup=ger_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="ger_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  250 600  UZS\n▶  Parvozdan keyin: 279 388 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_biz_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_ger_xalqaro_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_biz)

#ekonom klass uchun
@dp.callback_query_handler(text="vaqt_eko_ger")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=ger_vaqt_eko)


#3 kunlik tarif ekonom

@dp.callback_query_handler(text="ger_eko_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  14:00  /  \n🛬 Qo'nish vaqti  --  16:30\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Bagaj: mavjud emas  ❌\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nmavjud emas  ❌\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 300 712 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_nat_3kun_knopka)

@dp.callback_query_handler(text="ger_eko_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 135 990  UZS\
		\n\n🔙  Avaichiptani qaytarish \nRuxsat etilmaydi   ❌\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko)

#5 kunlik tarif
@dp.callback_query_handler(text="ger_eko_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  05:45  /  \n🛬 Qo'nish vaqti  --  09:40\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Bagaj: mavjud emas  ❌\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ❌\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 300 712 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_nat_5kun_knopka)

@dp.callback_query_handler(text="ger_eko_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS  UZS\n▶  Parvozdan keyin: 136 800 UZS\
		\n\n🔙  Avaichiptani qaytarish: \nRuxsat etilmaydi   ❌\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko)

#7 kunlik tarif
@dp.callback_query_handler(text="ger_eko_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  05:45  /  \n🛬 Qo'nish vaqti  --  09:40\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Bagaj: mavjud emas  ❌\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ❌\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 300 712 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_nat_7kun_knopka)

@dp.callback_query_handler(text="ger_eko_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660   UZS\n▶  Parvozdan keyin: 183 990 UZS UZS\
		\n\n🔙  Avaichiptani qaytarish: \nRuxsat etilmaydi   ❌\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko)

#ekonom+ klass uchun
@dp.callback_query_handler(text="vaqt_eko_plus_ger")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=ger_vaqt_eko_plus)

#3 kunlik tarif ekonom plus
@dp.callback_query_handler(text="ger_eko_plus_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  05:45  /  \n🛬 Qo'nish vaqti  --  09:40\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 834 286 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="ger_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko_plus)

#5 kunlik tarif
@dp.callback_query_handler(text="ger_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  05:45  /  \n🛬 Qo'nish vaqti  --  09:40\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 810 800 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="ger_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko_plus)

#7 kunlik tarif
@dp.callback_query_handler(text="ger_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Fankfurt\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  05:45  /  \n🛬 Qo'nish vaqti  --  09:40\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar \n▶️  Maksimal vazni: 8kg \
		\n\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 770 250  UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="ger_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS UZS\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_plus_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_plus_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko_plus)















@dp.callback_query_handler(text="ist")
async def far_urg(call:CallbackQuery):
	await call.message.reply("Tarifni tanlang", reply_markup=tarif_ist)


#Toshkent - Istanbul yo'nalishga safar
#biznes klass uchun 
@dp.callback_query_handler(text="vaqt_biz_ist")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=ist_vaqt_biz)

@dp.callback_query_handler(text="ort_xalqaro")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Quyidagi davlatlarga parvozlar mavjud", reply_markup=xalqaro)


#3 kunlik tarif biznes
@dp.callback_query_handler(text="ort_ist_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_ist)

@dp.callback_query_handler(text="ist_biz_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  🔽\
		\n🛫  Uchib Ketish vaqti: 20:25    \n🛬 Qo'nish vaqti  --  21:55\
		\nToshkent - Istanbul  🔽\
		\n🛫  Uchib Ketish vaqti: 09:25    \n🛬 Qo'nish vaqti  --  11:45\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 4489 ball\
		\nChipta narxi - 8 475 135 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="ist_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\n▶  Parvozdan oldin:  98 128 UZS \n▶  Parvozdan keyin: 98 128 UZS\
		\nToshkent - Istanbul:\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ist_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ist_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_biz)


#5 kunlik tarif biznes
@dp.callback_query_handler(text="ist_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  🔽\
		\n🛫  Uchib Ketish vaqti: 20:25    \n🛬 Qo'nish vaqti  --  21:55\
		\nToshkent - Istanbul  🔽\
		\n🛫  Uchib Ketish vaqti: 09:25    \n🛬 Qo'nish vaqti  --  11:45\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 4865 ball\
		\nChipta narxi - 8 329 900 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="ist_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\n▶  Parvozdan oldin:  98 128 UZS \n▶  Parvozdan keyin: 98 128 UZS\
		\nToshkent - Istanbul:\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ist_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ist_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_biz)


#7 kunlik tarif biznes
@dp.callback_query_handler(text="ort_ist_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_ist)

@dp.callback_query_handler(text="ist_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  🔽\
		\n🛫  Uchib Ketish vaqti: 06:45    \n🛬 Qo'nish vaqti  --  07:40\
		\nToshkent - Istanbul  🔽\
		\n🛫  Uchib Ketish vaqti: 08:55    \n🛬 Qo'nish vaqti  --  11:55\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 4865 ball\
		\nChipta narxi - 7 705 796 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="ist_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\n▶  Parvozdan oldin:  98 128 UZS \n▶  Parvozdan keyin: 98 128 UZS\
		\nToshkent - Istanbul:\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ist_biz_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_ist_xalqaro_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_biz)

#ekonom klass uchun
@dp.callback_query_handler(text="vaqt_eko_ist")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=ist_vaqt_eko)



#3 kunlik tarif ekonom
@dp.callback_query_handler(text="ist_eko_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  🔽\
		\n🛫  Uchib Ketish vaqti: 06:45    \n🛬 Qo'nish vaqti  --  07:40\
		\nToshkent - Istanbul  🔽\
		\n🛫  Uchib Ketish vaqti: 08:55    \n🛬 Qo'nish vaqti  --  11:55\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 3475 ball\
		\nChipta narxi - 4 529 172 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_eko_nat_3kun_knopka)

@dp.callback_query_handler(text="ist_eko_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\n▶  Parvozdan oldin:  12 266 UZS \n▶  Parvozdan keyin: 36 798 UZS\
		\nToshkent - Istanbul:\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 367 980 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ist_eko_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ist_eko_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_eko)

#5 kunlik tarif
@dp.callback_query_handler(text="ist_eko_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  🔽\
		\n🛫  Uchib Ketish vaqti: 06:45    \n🛬 Qo'nish vaqti  --  07:40\
		\nToshkent - Istanbul  🔽\
		\n🛫  Uchib Ketish vaqti: 08:55    \n🛬 Qo'nish vaqti  --  11:55\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 3475 ball\
		\nChipta narxi - 4 320 550 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_eko_nat_5kun_knopka)

@dp.callback_query_handler(text="ist_eko_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\n▶  Parvozdan oldin:  12 266 UZS \n▶  Parvozdan keyin: 36 798 UZS\
		\nToshkent - Istanbul:\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 367 980 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ist_eko_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ist_eko_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_eko)

#7 kunlik tarif
@dp.callback_query_handler(text="ist_eko_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  🔽\
		\n🛫  Uchib Ketish vaqti: 06:45    \n🛬 Qo'nish vaqti  --  07:40\
		\nToshkent - Istanbul  🔽\
		\n🛫  Uchib Ketish vaqti: 08:55    \n🛬 Qo'nish vaqti  --  11:55\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 4200 ball\
		\nChipta narxi - 5 110 889 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_eko_nat_7kun_knopka)

@dp.callback_query_handler(text="ist_eko_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\n▶  Parvozdan oldin:  12 266 UZS \n▶  Parvozdan keyin: 36 798 UZS\
		\nToshkent - Istanbul:\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 367 980 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=ist_eko_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_ist_eko_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_eko)













@dp.callback_query_handler(text="rim")
async def far_urg(call:CallbackQuery):
	await call.message.reply("Tarifni tanlang", reply_markup=tarif_rim)

#Toshkent - Rim yo'nalishga safar

@dp.callback_query_handler(text="ort_xalqaro")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Quyidagi davlatlarga parvozlar mavjud", reply_markup=xalqaro)

#ekonom klass uchun
@dp.callback_query_handler(text="ort_rim_eko_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_rim)

@dp.callback_query_handler(text="vaqt_eko_rim")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=rim_vaqt_eko)


#3 kunlik tarif ekonom

@dp.callback_query_handler(text="rim_eko_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Rim\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  08:30  /  \n🛬 Qo'nish vaqti  --  12:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Bagaj: mavjud emas  ❌\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nmavjud emas  ❌\
		\n\nUzairplus - 3638 ball\
		\nChipta narxi - 4 814 571 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_nat_3kun_knopka)

@dp.callback_query_handler(text="rim_eko_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 135 990  UZS\
		\n\n🔙  Avaichiptani qaytarish \nRuxsat etilmaydi   ❌\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko)

#5 kunlik tarif
@dp.callback_query_handler(text="rim_eko_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Rim\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  08:30  /  \n🛬 Qo'nish vaqti  --  12:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Bagaj: mavjud emas  ❌\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nmavjud emas  ❌\
		\n\nUzairplus - 3890 ball\
		\nChipta narxi - 4 990 500 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_nat_5kun_knopka)

@dp.callback_query_handler(text="rim_eko_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS  UZS\n▶  Parvozdan keyin: 136 800 UZS\
		\n\n🔙  Avaichiptani qaytarish: \nRuxsat etilmaydi   ❌\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko)

#7 kunlik tarif
@dp.callback_query_handler(text="rim_eko_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Rim\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  08:30  /  \n🛬 Qo'nish vaqti  --  12:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Bagaj: mavjud emas  ❌\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nmavjud emas  ❌\
		\n\nUzairplus - 3890 ball\
		\nChipta narxi - 4 769 880 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_nat_7kun_knopka)

@dp.callback_query_handler(text="rim_eko_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS  so'm\n▶  Parvozdan keyin: 183 990 UZS so'm\
		\n\n🔙  Avaichiptani qaytarish: \nRuxsat etilmaydi   ❌\
		\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko)

#ekonom+ klass uchun
@dp.callback_query_handler(text="vaqt_eko_plus_rim")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=rim_vaqt_eko_plus)

#3 kunlik tarif ekonom plus
@dp.callback_query_handler(text="rim_eko_plus_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Rim\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  08:30  /  \n🛬 Qo'nish vaqti  --  12:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 3890 ball\
		\nChipta narxi - 8 516 763 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="rim_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko_plus)

#5 kunlik tarif
@dp.callback_query_handler(text="rim_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Rim\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  08:30  /  \n🛬 Qo'nish vaqti  --  12:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 3638 ball\
		\nChipta narxi - 8 616 800 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="rim_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko_plus)

#7 kunlik tarif
@dp.callback_query_handler(text="rim_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Rim\
		\n✈️  Samolyot modeli  --  Airbus  320  Neo\
		\n🛫  Uchib Ketish vaqti  --  08:30  /  \n🛬 Qo'nish vaqti  --  12:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \n▶️  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus - 3890 ball\
		\nChipta narxi - 8 450 800 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="rim_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_plus_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_plus_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko_plus)













@dp.callback_query_handler(text="baa")
async def far_urg(call:CallbackQuery):
	await call.message.reply("Tarifni tanlang", reply_markup=tarif_baa)

#Toshkent - Dubay yo'nalishga safar
#biznes klass uchun 
@dp.callback_query_handler(text="vaqt_biz_baa")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=baa_vaqt_biz)

@dp.callback_query_handler(text="ort_xalqaro")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Quyidagi davlatlarga parvozlar mavjud", reply_markup=xalqaro)


#3 kunlik tarif biznes
@dp.callback_query_handler(text="ort_baa_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_baa)

@dp.callback_query_handler(text="baa_biz_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Dubay\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 08:25    \n🛬 Qo'nish vaqti  --  11:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 40kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  4950 ball\
		\nChipta narxi - 12 535 865 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="baa_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=baa_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_baa_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_biz)


#5 kunlik tarif biznes
@dp.callback_query_handler(text="baa_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Dubay\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 08:25    \n🛬 Qo'nish vaqti  --  11:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 40kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  4950 ball\
		\nChipta narxi - 11 835 876 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="baa_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=baa_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_baa_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_biz)


#7 kunlik tarif biznes

@dp.callback_query_handler(text="baa_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Dubay\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 08:25    \n🛬 Qo'nish vaqti  --  11:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 40kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  4950 ball\
		\nChipta narxi - 13 050 000 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="baa_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=baa_biz_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_baa_xalqaro_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_biz)



#3 kunlik tarif ekonom plus
@dp.callback_query_handler(text="vaqt_eko_plus_baa")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=baa_vaqt_eko_plus)

@dp.callback_query_handler(text="baa_eko_plus_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Dubay\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 08:25    \n🛬 Qo'nish vaqti  --  11:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 30kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  3300 ball\
		\nChipta narxi - 4 581 895 UZS\nTarif:  <ins>ekonom  +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="baa_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=baa_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_baa_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_eko_plus)

#5 kunlik tarif
@dp.callback_query_handler(text="baa_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Dubay\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 08:25    \n🛬 Qo'nish vaqti  --  11:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 30kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  3500 ball\
		\nChipta narxi - 5 220 830 UZS\nTarif:  <ins>ekonom  +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="baa_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=baa_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_baa_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_eko_plus)

#7 kunlik tarif
@dp.callback_query_handler(text="baa_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - Dubay\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 09:25    \n🛬 Qo'nish vaqti  --  12:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 30kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  3700 ball\
		\nChipta narxi - 4 990 830 UZS\nTarif:  <ins>ekonom  +</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="baa_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=baa_eko_plus_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_baa_eko_plus_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_eko_plus)












@dp.callback_query_handler(text="lon")
async def far_urg(call:CallbackQuery):
	await call.message.reply("Tarifni tanlang", reply_markup=tarif_bb)


#Toshkent - Dubay yo'nalishga safar
#biznes klass uchun 
@dp.callback_query_handler(text="vaqt_biz_bb")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=bb_vaqt_biz)

@dp.callback_query_handler(text="ort_xalqaro")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Quyidagi davlatlarga parvozlar mavjud", reply_markup=xalqaro)


#3 kunlik tarif biznes
@dp.callback_query_handler(text="ort_bb_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_bb)

@dp.callback_query_handler(text="bb_biz_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - London\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 10:45    \n🛬 Qo'nish vaqti  --  14:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  7893 ball\
		\nChipta narxi - 10 956 874 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="bb_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=bb_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_bb_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_biz)


#5 kunlik tarif biznes
@dp.callback_query_handler(text="bb_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - London\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 10:45    \n🛬 Qo'nish vaqti  --  14:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  7900 ball\
		\nChipta narxi - 11 156 574 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="bb_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=bb_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_bb_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_biz)


#7 kunlik tarif biznes

@dp.callback_query_handler(text="bb_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - London\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 10:45    \n🛬 Qo'nish vaqti  --  14:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 10kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 32kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  8392 ball\
		\nChipta narxi - 12 000 500 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="bb_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  122 660 UZS \n▶  Parvozdan keyin: 183 990 UZS\
		\n\n🔙  Avaichiptani qaytarish  613 300 UZS  so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=bb_biz_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_bb_xalqaro_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_biz)



#3 kunlik tarif ekonom plus
@dp.callback_query_handler(text="vaqt_eko_plus_bb")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=bb_vaqt_eko_plus)

@dp.callback_query_handler(text="bb_eko_plus_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - London\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 10:45    \n🛬 Qo'nish vaqti  --  14:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  5200 ball\
		\nChipta narxi - 7 892 592 UZS\nTarif:  <ins>ekonom  +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="bb_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=bb_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_bb_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_eko_plus)

#5 kunlik tarif eko plus
@dp.callback_query_handler(text="bb_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - London\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 10:45    \n🛬 Qo'nish vaqti  --  14:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  5200 ball\
		\nChipta narxi - 7 892 592 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="bb_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=bb_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_bb_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_eko_plus)

#7 kunlik tarif eko plus
@dp.callback_query_handler(text="bb_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("📍  Yo'nalish:  Toshkent - London\
		\n✈️  Samolyot modeli  --  Airbus  320 Neo\
		\n🛫  Uchib Ketish vaqti: 10:45    \n🛬 Qo'nish vaqti  --  14:00\
		\n\n👝❗️  Qo'l yuki uchun qo'yilgan talablar  \n▶️  Maksimal vazni: 8kg \
		\n🧳❗  Maksimal bagaj sig'imi \n▶️  Maksimal vazni: 23kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ✅\
		\nChiptani qaytarish imkoniyati: \nMavjud  ✅\
		\n\nUzairplus -  5200 ball\
		\nChipta narxi - 8 127 430 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="bb_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("📃  🖋  Aviachiptani qayta rasmiylashtirish\
		\n▶  Parvozdan oldin:  245 320 UZS \n▶  Parvozdan keyin: 227 980 UZS\
		\n\n🔙  Avaichiptani qaytarish 520 300 UZS so'm\n➕  Parvozga bir soat oldin kelmaslik", reply_markup=bb_eko_plus_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_bb_eko_plus_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_eko_plus)


@dp.message_handler(text="Ortga     ⤴️")
async def ortga_tarif(message:types. Message):
	await message.reply("Tarifni tanlang", reply_markup=xalqaro)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
