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
ADMIN =ADMIN'S ID HERE


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \nā šŗ  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz š¤µāāš¤µāā",reply_markup=bosh_menyu)
    x.create_table()

#Kontakt va ijtimoiy tarmoq haqida malumot beruvchi tag tugmalar

@dp.message_handler(text="š Kontaktlarimiz")
async def kontakt(message: types.Message):
	await message.answer("<b>Kontaktlar</b> \n\n<b>Aloqa markazi</b>\n+998781400200\n<ins>kecha-kunduz</ins>\
		\n\n<b>Ishonch telefoni</b>\n+998781204770\n<ins>Har kuni: 9:00 - 18:00 gacha</ins>", parse_mode='HTML')

@dp.message_handler(text="š² Ijtimoiy tarmoqlardagi manzilimiz")
async def ijtimoiy(message: types.Message):
	await message.answer("<b>Uzbekistan Airways ijtimoiy tarmoqlarda</b>\
		\n\n<ins>Instagram:</ins> \
		https://www.instagram.com/uzairways/ \
		\n\n<ins>Telegram:</ins> https://t.me/uzbekistanairways \
		\n\n<ins>Facebook:</ins> https://www.facebook.com/\
		uzairways.official/\
		\n\n<ins>You Tube:</ins> https://www.youtube.com/c/UzbekistanAirwaysHY \
		\n\n<ins>Linked in:</ins> https://www.linkedin.com/company/uzbekistan-airways-jsc", parse_mode='HTML')

@dp.message_handler(text="Asosiy menyuga    āļø")
async def ortga(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \nā šŗ  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz š¤µāāš¤µāā",reply_markup=bosh_menyu)
	
#Buyurtma berish qismi

@dp.message_handler(text="š« Online chipta buyurtma berish")
async def chipta(message: types.Message):
	await message.answer("Parvoz turini tanlang  [Mahalliy/ Xalqaro]  š½",reply_markup=buyurtma)

#Mahalliy parvozga buyurtma berish

@dp.message_handler(text="āļø  šŗšæ š  Mahalliy parvoz")
async def mahaliy(message: types.Message):
	await message.answer("Quyidagi shaharlarga parvozlar mavjud", reply_markup=mahalliy)

#Mahalliy tariflar vaqtlari Toshkent - Samarqand 
@dp.callback_query_handler(text="ort_buyurtma")
async def tosh_sam(call:CallbackQuery):
	await call.message.answer("Parvoz turini tanlang  [Mahalliy/ Xalqaro]  š½",reply_markup=buyurtma)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Samarqand\
		\nš«  Uchib Ketish vaqti  --  11:20  /  \nš¬ Qo'nish vaqti  --  12:30\
		\n\nš§³āļø  Qo'l yuki uchun qo'yilgan talablar  š½\nMaksimal vazni: 18kg / \nMaksimal hajmi: 180sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 1000 ball\
		\nChipta narxi - 720 500 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=tosh_biz_nat_kun_knopka)

@dp.callback_query_handler(text="tosh_biz_nat_kun_jarima")
async def tosh_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  36 550  UZS\nParvozdan keyin: 38 379 UZS\
		\n\nš  Avaichiptani qaytarish  45 770  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=tosh_biz_nat_kun_roziman)

@dp.callback_query_handler(text="ort_mahalliy_kun_qismi")
async def tosh_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=tosh_vaqt_biz)


#kechki tarif
@dp.callback_query_handler(text="tosh_biz_nat_kech")
async def tosh_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Samarqand\
		\nš«  Uchib Ketish vaqti  --  19:20  /  \nš¬ Qo'nish vaqti  --  20:30\
		\n\nš§³āļø  Qo'l yuki uchun qo'yilgan talablar  š½\nMaksimal vazni: 18kg / \nMaksimal hajmi: 180sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 1000 ball\
		\nChipta narxi - 720 500 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=tosh_biz_nat_kech_knopka)

@dp.callback_query_handler(text="tugat")
async def tosh_kun_tugat(call:CallbackQuery):
	await call.message.reply("<ins>š  Tabriklaymiz!!!</ins>\
	\n<b>Siz [Uzbekistan Airways] ning \nSovrinli aviachipta o'yini ishtirokchisiga aylandigiz</b> āļøāļøāļø, \
	\n\nQuyida telefon raqamingizni qoldiring...",\
	parse_mode='HTML',reply_markup=tel)

@dp.message_handler(content_types=['contact'])
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
		
		await message.answer("ā  Sizning ma'lumotlaringiz qabul qilib olindi\
			\n\nHaridingiz uchun rahmat !! \nCall center bo'limi siz bilan tez orada bog'lanadi...š", \
			reply_markup=qayta)
	else:
		await message.answer("ā  Sizning ma'lumotlaringiz qabul qilib olindi\
			\n\nHaridingiz uchun rahmat !! \nCall center bo'limi siz bilan tez orada bog'lanadi...š", \
			reply_markup=qayta)

@dp.message_handler(commands='Alluser', user_id=[ADMIN'S ID HERE])
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

@dp.message_handler(commands='all', user_id=1344241185)
async def userss(message: types.Message):
	user_id =message.from_user.id
	user =x.users(user_id)
	await bot.send_message(ADMIN, users)

@dp.callback_query_handler(text="tosh_biz_nat_kech_jarima")
async def tosh_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  36 550  UZS\nParvozdan keyin: 38 379 UZS\
		\n\nš  Avaichiptani qaytarish  45 770  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=tosh_biz_nat_kech_roziman)

@dp.message_handler(text='š  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \nā šŗ  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz š¤µāāš¤µāā",reply_markup=bosh_menyu)



#ekonom klass uchun (kunduzgi)
@dp.callback_query_handler(text="vaqt_eko_tosh")
async def tosh_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=tosh_vaqt_eko)

#kunduzgi tarif 
@dp.callback_query_handler(text="tosh_eko_nat_kun")
async def tosh_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Samarqand\
		\nš«  Uchib Ketish vaqti  --  09:00  /  \nš¬ Qo'nish vaqti  --  11:30\
		\n\nš§³āāļø  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ā\
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
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  36 550  UZS\nParvozdan keyin: 38 379 UZS\
		\n\nš  Avaichiptani qaytarish  45 770  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=tosh_eko_nat_kun_roziman)

#kechki tarif
@dp.callback_query_handler(text="tosh_eko_nat_kech")
async def tosh_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Samarqand\
		\nš«  Uchib Ketish vaqti  --  21:00  /  \nš¬ Qo'nish vaqti  --  22:30\
		\n\nš§³āāļø  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ā\
		\n\nUzairplus - 800 ball\
		\nChipta narxi - 637 606 UZS,\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=tosh_eko_nat_kech_knopka)

@dp.callback_query_handler(text="tosh_eko_nat_kech_jarima")
async def tosh_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  27 500  UZS\nParvozdan keyin: 35 380 UZS\
		\n\nš  Avaichiptani qaytarish:  Parvozdan keyin tarif shuningdek, YQ, YQ yigāimlari to'liq ushlab qolinadi. Aeroport yigāmlari va boshqa toālovlar qaytariladi.\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=tosh_eko_nat_kech_roziman)

@dp.message_handler(text='š  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \nā šŗ  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz š¤µāāš¤µāā",reply_markup=bosh_menyu)




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
	await call.message.answer("š  Yo'alish:  Farg'ona - Urganch\
		\nš«  Uchib Ketish vaqti  --  12:20  /  \nš¬ Qo'nish vaqti  --  14:10\
		\n\nš§³āļø  Qo'l yuki uchun qo'yilgan talablar  š½\nMaksimal vazni: 16kg / \nMaksimal hajmi: 140sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 1200 ball\
		\nChipta narxi - 890 384 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=far_biz_nat_kun_biz)

@dp.callback_query_handler(text="far_biz_nat_kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  122 660  UZS\nParvozdan keyin: 143 388 UZS\
		\n\nš  Avaichiptani qaytarish  165 770  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=far_biz_nat_kun_roziman)

@dp.callback_query_handler(text="ort_far_mahalliy_kun_qismi")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=far_vaqt_biz)

@dp.callback_query_handler(text="ort_far_eko_mahalliy_kun_qismi")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=far_vaqt_eko)

#kechki tarif
@dp.callback_query_handler(text="far_biz_nat_kech")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish: Farg'ona - Urganch\
		\nš«  Uchib Ketish vaqti  --  20:25  /  \nš¬ Qo'nish vaqti  --  21:55\
		\n\nš§³āļø  Qo'l yuki uchun qo'yilgan talablar  š½\nMaksimal vazni: 16kg / \nMaksimal hajmi: 140sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 1000 ball\
		\nChipta narxi - 879 550 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=far_biz_nat_kech_biz)

@dp.callback_query_handler(text="far_biz_nat_kech_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  122 660  UZS\nParvozdan keyin: 143 388 UZS\
		\n\nš  Avaichiptani qaytarish  165 770  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=far_biz_nat_kech_roziman)


@dp.message_handler(text='š  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \nā šŗ  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz š¤µāāš¤µāā",reply_markup=bosh_menyu)



#ekonom klass uchun (kunduzgi)
@dp.callback_query_handler(text="vaqt_eko_far")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=far_vaqt_eko)

#kunduzgi tarif 
@dp.callback_query_handler(text="far_eko_nat_kun")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Farg'ona - Urganch\
		\nš«  Uchib Ketish vaqti  --  12:20  /  \nš¬ Qo'nish vaqti  --  14:10\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ā\
		\n\nUzairplus - 900 ball\
		\nChipta narxi - 740 284 UZS,\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=far_eko_kun_knopka)

@dp.callback_query_handler(text="far_eko_nat_kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  122 660  UZS\nParvozdan keyin: 143 388 UZS\
		\n\nš  Avaichiptani qaytarish: \nRuxsat etilmaydi  ā\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=far_eko_nat_kun_roziman)

#kechki tarif
@dp.callback_query_handler(text="far_eko_nat_kech")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Farg'ona - Urganch\
		\nš«  Uchib Ketish vaqti  --  20:00  /  \nš¬ Qo'nish vaqti  --  21:20\
		\n\nš§³āāļø  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ā\
		\n\nUzairplus - 900 ball\
		\nChipta narxi - 740 284 UZS,\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=far_eko_kech_knopka)

@dp.callback_query_handler(text="far_eko_nat_kech_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  122 660  UZS\nParvozdan keyin: 143 388 UZS\
		\n\nš  Avaichiptani qaytarish  \nRuxsat etilmaydi  ā\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=far_eko_nat_kech_roziman)


@dp.message_handler(text='š  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \nā šŗ  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz š¤µāāš¤µāā",reply_markup=bosh_menyu)


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
	await call.message.answer("š  Yo'nalish:  Qarshi - Namangan\
		\nš«  Uchib Ketish vaqti  --  10:30  /  \nš¬ Qo'nish vaqti  --  12:20\
		\n\nš§³āļø  Qo'l yuki uchun qo'yilgan talablar  š½\nMaksimal vazni: 19kg / \nMaksimal hajmi: 200sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 900 ball\
		\nChipta narxi - 649 324 UZS\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=qar_biz_nat_kun_knopka)

@dp.callback_query_handler(text="qar_biz_nat_kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  35 639  UZS\nParvozdan keyin: 39 388 UZS\
		\n\nš  Avaichiptani qaytarish  55 750  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=qar_biz_nat_kun_roziman)

@dp.callback_query_handler(text="ort_qar_mahalliy_kun_qismi")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=qar_vaqt_biz)

@dp.callback_query_handler(text="ort_qar_eko_mahalliy_kun_qismi")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=qar_vaqt_eko)

#kechki tarif
@dp.callback_query_handler(text="qar_biz_nat_kech")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish: Qarshi - Namangan\
		\nš«  Uchib Ketish vaqti  --  19:25  /  \nš¬ Qo'nish vaqti  --  20:35\
		\n\nš§³āļø  Qo'l yuki uchun qo'yilgan talablar  š½\nMaksimal vazni: 19kg / \nMaksimal hajmi: 200sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 900 ball\
		\nChipta narxi - 624 550 UZS,\nTarif:  <ins>biznes</ins>",parse_mode='HTML', reply_markup=qar_biz_nat_kech_knopka)

@dp.callback_query_handler(text="qar_biz_nat_kech_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  35 639  UZS\nParvozdan keyin: 39 388 UZS\
		\n\nš  Avaichiptani qaytarish  55 750  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=qar_biz_nat_kech_roziman)


@dp.message_handler(text='š  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \nā šŗ  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz š¤µāāš¤µāā",reply_markup=bosh_menyu)



#ekonom klass uchun (kunduzgi)
@dp.callback_query_handler(text="vaqt_eko_qar")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Kunning qaysi qismida uchib ketasiz ? ", reply_markup=qar_vaqt_eko)

#kunduzgi tarif 
@dp.callback_query_handler(text="qar_eko_nat_kun")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Qarshi - Namangan\
		\nš«  Uchib Ketish vaqti  --  12:00  /  \nš¬ Qo'nish vaqti  --  13:20\
		\n\nš§³āāļø  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ā\
		\n\nUzairplus - 600 ball\
		\nChipta narxi - 534 284 UZS\nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=qar_eko_nat_kun_knopka)

@dp.callback_query_handler(text="qar_eko_nat_kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  25 300  UZS\nParvozdan keyin: 33 480 UZS\
		\n\nš  Avaichiptani qaytarish:  Parvozdan keyin tarif shuningdek, YQ, YQ yigāimlari to'liq ushlab qolinadi. Aeroport yigāmlari va boshqa toālovlar qaytariladi.\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=qar_eko_nat_kun_roziman)

#kechki tarif
@dp.callback_query_handler(text="qar_eko_nat_kech")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Qarshi - Namangan\
		\nš«  Uchib Ketish vaqti  --  20:00  /  \nš¬ Qo'nish vaqti  --  21:20\
		\n\nš§³āāļø  Qo'l yuki bagaji mavjud emas\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ā\
		\n\nUzairplus - 600 ball\
		\nChipta narxi - 554 300 UZS \nTarif:  <ins>ekonom</ins>",parse_mode='HTML', reply_markup=qar_eko_nat_kech_knopka)

@dp.callback_query_handler(text="qar_eko_nat_kech_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  š  š  Aviachiptani qayta rasmiylashtirish  š½\
		\nParvozdan oldin:  25 300  UZS\nParvozdan keyin: 33 480 UZS\
		\n\nš  Avaichiptani qaytarish:  Parvozdan keyin tarif shuningdek, YQ, YQ yigāimlari to'liq ushlab qolinadi. Aeroport yigāmlari va boshqa toālovlar qaytariladi.\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=qar_eko_nat_kech_roziman)


@dp.message_handler(text='š  Qayta harid qilish')
async def qayta_harid(message: types.Message):
	await message.answer(f"Assalomu aleykum hurmatli {message.from_user.full_name}\
      \nā šŗ  Uzbekistan Airways ga xush kelibsiz \nSizga qanday yordam bera olamiz š¤µāāš¤µāā",reply_markup=bosh_menyu)









#Xalqaro parvozga buyurtma berish
@dp.message_handler(text="āļø  š š  Xalqaro parvoz")
async def xaqaro(message: types.Message):
	await message.answer("Quyidagi davlatlarga parvozlar mavjud", reply_markup=xalqaro)

@dp.callback_query_handler(text="ort_buyurtma")
async def xaqaro(call:CallbackQuery):
	await call.message.answer("Parvoz turini tanlang  [Mahalliy/ Xalqaro]  š½",reply_markup=buyurtma)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  14:00  /  \nš¬ Qo'nish vaqti  --  16:30\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 1005 ball\
		\nChipta narxi - 7 312 307 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="kz_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  170 600  UZS\nā¶  Parvozdan keyin: 185 388 UZS\
		\n\nš  Avaichiptani qaytarish  245 320 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_kz_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_biz)

#5 kunlik tarif biznes
@dp.callback_query_handler(text="ort_kz_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_kz)

@dp.callback_query_handler(text="kz_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  15:50  /  \nš¬ Qo'nish vaqti  --  18:20\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 10kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 1000 ball\
		\nChipta narxi - 7 861 990\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="kz_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  171 400  UZS\nā¶  Parvozdan keyin: 183 989 UZS\
		\n\nš  Avaichiptani qaytarish  264 320 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_kz_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_biz)

#7 kunlik tarif biznes
@dp.callback_query_handler(text="ort_kz_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_kz)

@dp.callback_query_handler(text="kz_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  14:00  /  \nš¬ Qo'nish vaqti  --  16:30\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 10kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 938 ball\
		\nChipta narxi - 6 037 341 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>bir hafta ichida</ins>",parse_mode='HTML', reply_markup=kz_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="kz_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS  UZS\nā¶  Parvozdan keyin: 183 990 UZS UZS\
		\n\nš  Avaichiptani qaytarish  245 320 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_biz_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  14:00  /  \nš¬ Qo'nish vaqti  --  16:30\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 670 ball\
		\nChipta narxi - 4 762 375 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_nat_3kun_knopka)

@dp.callback_query_handler(text="kz_eko_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 135 990  UZS\
		\n\nš  Avaichiptani qaytarish 245 320 UZS UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko)

#5 kunlik tarif
@dp.callback_query_handler(text="kz_eko_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  07:30  /  \nš¬ Qo'nish vaqti  --  10:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 603 ball\
		\nChipta narxi - 3 087 419 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_nat_5kun_knopka)

@dp.callback_query_handler(text="kz_eko_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS  UZS\nā¶  Parvozdan keyin: 136 800 UZS\
		\n\nš  Avaichiptani qaytarish  245 320 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko)

#7 kunlik tarif
@dp.callback_query_handler(text="kz_eko_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  14:00  /  \nš¬ Qo'nish vaqti  --  16:30\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 670 ball\
		\nChipta narxi - 3 824 900 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>bir hafta ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_nat_7kun_knopka)

@dp.callback_query_handler(text="kz_eko_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS  UZS\nā¶  Parvozdan keyin: 183 990 UZS UZS\
		\n\nš  Avaichiptani qaytarish  245 320 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  12:00  /  \nš¬ Qo'nish vaqti  --  14:30\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 27kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 800 ball\
		\nChipta narxi - 5 862 370 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="kz_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 135 990  UZS\
		\n\nš  Avaichiptani qaytarish 245 320 UZS UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko_plus)

#5 kunlik tarif ekonom plus
@dp.callback_query_handler(text="kz_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  09:00  /  \nš¬ Qo'nish vaqti  --  12:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 27kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 805 ball\
		\nChipta narxi - 4 687 420 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="kz_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS  UZS\nā¶  Parvozdan keyin: 136 800 UZS\
		\n\nš  Avaichiptani qaytarish  245 320 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_kz_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=kz_vaqt_eko_plus)

#7 kunlik tarif
@dp.callback_query_handler(text="kz_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Qozog'iston\
		\nāļø  Samolyot modeli  --  Airbus  320\
		\nš«  Uchib Ketish vaqti  --  14:00  /  \nš¬ Qo'nish vaqti  --  16:30\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 27kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 870 ball\
		\nChipta narxi - 4 850 900 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>bir hafta ichida</ins>",parse_mode='HTML', reply_markup=kz_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="kz_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS  UZS\nā¶  Parvozdan keyin: 183 990 UZS UZS\
		\n\nš  Avaichiptani qaytarish  245 320 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=kz_eko_plus_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti  --  05:45  /  \nš¬ Qo'nish vaqti  --  09:40\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: P2-8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 7032 ball\
		\nChipta narxi - 19 047 340 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="ger_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  250 600  UZS\nā¶  Parvozdan keyin: 279 388 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ger_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_biz)

#5 kunlik tarif biznes
@dp.callback_query_handler(text="ort_ger_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_ger)

@dp.callback_query_handler(text="ger_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti  --  05:45  /  \nš¬ Qo'nish vaqti  --  09:40\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: P2-8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 7032 ball\
		\nChipta narxi - 19 047 340 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="ger_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  250 600  UZS\nā¶  Parvozdan keyin: 279 388 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ger_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_biz)

#7 kunlik tarif biznes
@dp.callback_query_handler(text="ort_ger_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_ger)

@dp.callback_query_handler(text="ger_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent -  Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  05:45  /  \nš¬ Qo'nish vaqti  --  09:40\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: P2-8kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 6563 ball\
		\nChipta narxi - 11 366 360 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>bir hafta ichida</ins>",parse_mode='HTML', reply_markup=ger_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="ger_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  250 600  UZS\nā¶  Parvozdan keyin: 279 388 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_biz_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  14:00  /  \nš¬ Qo'nish vaqti  --  16:30\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Bagaj: mavjud emas  ā\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nmavjud emas  ā\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 300 712 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_nat_3kun_knopka)

@dp.callback_query_handler(text="ger_eko_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 135 990  UZS\
		\n\nš  Avaichiptani qaytarish \nRuxsat etilmaydi   ā\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko)

#5 kunlik tarif
@dp.callback_query_handler(text="ger_eko_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  05:45  /  \nš¬ Qo'nish vaqti  --  09:40\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Bagaj: mavjud emas  ā\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ā\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 300 712 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_nat_5kun_knopka)

@dp.callback_query_handler(text="ger_eko_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS  UZS\nā¶  Parvozdan keyin: 136 800 UZS\
		\n\nš  Avaichiptani qaytarish: \nRuxsat etilmaydi   ā\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko)

#7 kunlik tarif
@dp.callback_query_handler(text="ger_eko_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  05:45  /  \nš¬ Qo'nish vaqti  --  09:40\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Bagaj: mavjud emas  ā\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud emas  ā\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 300 712 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_nat_7kun_knopka)

@dp.callback_query_handler(text="ger_eko_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660   UZS\nā¶  Parvozdan keyin: 183 990 UZS UZS\
		\n\nš  Avaichiptani qaytarish: \nRuxsat etilmaydi   ā\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  05:45  /  \nš¬ Qo'nish vaqti  --  09:40\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 834 286 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="ger_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko_plus)

#5 kunlik tarif
@dp.callback_query_handler(text="ger_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  05:45  /  \nš¬ Qo'nish vaqti  --  09:40\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 810 800 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="ger_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ger_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ger_vaqt_eko_plus)

#7 kunlik tarif
@dp.callback_query_handler(text="ger_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Fankfurt\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  05:45  /  \nš¬ Qo'nish vaqti  --  09:40\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar \nā¶ļø  Maksimal vazni: 8kg \
		\n\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 3750 ball\
		\nChipta narxi - 3 770 250  UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=ger_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="ger_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS UZS\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ger_eko_plus_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  š½\
		\nš«  Uchib Ketish vaqti: 20:25    \nš¬ Qo'nish vaqti  --  21:55\
		\nToshkent - Istanbul  š½\
		\nš«  Uchib Ketish vaqti: 09:25    \nš¬ Qo'nish vaqti  --  11:45\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 4489 ball\
		\nChipta narxi - 8 475 135 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="ist_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\nā¶  Parvozdan oldin:  98 128 UZS \nā¶  Parvozdan keyin: 98 128 UZS\
		\nToshkent - Istanbul:\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ist_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ist_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_biz)


#5 kunlik tarif biznes
@dp.callback_query_handler(text="ist_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  š½\
		\nš«  Uchib Ketish vaqti: 20:25    \nš¬ Qo'nish vaqti  --  21:55\
		\nToshkent - Istanbul  š½\
		\nš«  Uchib Ketish vaqti: 09:25    \nš¬ Qo'nish vaqti  --  11:45\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 4865 ball\
		\nChipta narxi - 8 329 900 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="ist_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\nā¶  Parvozdan oldin:  98 128 UZS \nā¶  Parvozdan keyin: 98 128 UZS\
		\nToshkent - Istanbul:\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ist_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ist_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_biz)


#7 kunlik tarif biznes
@dp.callback_query_handler(text="ort_ist_xalqaro_tarif")
async def mahalliy_far_tarif(call:CallbackQuery):
	await call.message.answer("Tarifni tanlang", reply_markup=tarif_ist)

@dp.callback_query_handler(text="ist_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  š½\
		\nš«  Uchib Ketish vaqti: 06:45    \nš¬ Qo'nish vaqti  --  07:40\
		\nToshkent - Istanbul  š½\
		\nš«  Uchib Ketish vaqti: 08:55    \nš¬ Qo'nish vaqti  --  11:55\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 4865 ball\
		\nChipta narxi - 7 705 796 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="ist_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\nā¶  Parvozdan oldin:  98 128 UZS \nā¶  Parvozdan keyin: 98 128 UZS\
		\nToshkent - Istanbul:\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ist_biz_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  š½\
		\nš«  Uchib Ketish vaqti: 06:45    \nš¬ Qo'nish vaqti  --  07:40\
		\nToshkent - Istanbul  š½\
		\nš«  Uchib Ketish vaqti: 08:55    \nš¬ Qo'nish vaqti  --  11:55\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 3475 ball\
		\nChipta narxi - 4 529 172 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_eko_nat_3kun_knopka)

@dp.callback_query_handler(text="ist_eko_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\nā¶  Parvozdan oldin:  12 266 UZS \nā¶  Parvozdan keyin: 36 798 UZS\
		\nToshkent - Istanbul:\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 367 980 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ist_eko_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_ist_eko_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_eko)

#5 kunlik tarif
@dp.callback_query_handler(text="ist_eko_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  š½\
		\nš«  Uchib Ketish vaqti: 06:45    \nš¬ Qo'nish vaqti  --  07:40\
		\nToshkent - Istanbul  š½\
		\nš«  Uchib Ketish vaqti: 08:55    \nš¬ Qo'nish vaqti  --  11:55\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 3475 ball\
		\nChipta narxi - 4 320 550 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_eko_nat_5kun_knopka)

@dp.callback_query_handler(text="ist_eko_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\nā¶  Parvozdan oldin:  12 266 UZS \nā¶  Parvozdan keyin: 36 798 UZS\
		\nToshkent - Istanbul:\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 367 980 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ist_eko_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_ist_eko_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=ist_vaqt_eko)

#7 kunlik tarif
@dp.callback_query_handler(text="ist_eko_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Urganch  /\nUrganch - Istanbul\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\n\nToshkent - Urganch  š½\
		\nš«  Uchib Ketish vaqti: 06:45    \nš¬ Qo'nish vaqti  --  07:40\
		\nToshkent - Istanbul  š½\
		\nš«  Uchib Ketish vaqti: 08:55    \nš¬ Qo'nish vaqti  --  11:55\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 4200 ball\
		\nChipta narxi - 5 110 889 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=ist_eko_nat_7kun_knopka)

@dp.callback_query_handler(text="ist_eko_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\n\nToshkent - Urganch:\
		\nā¶  Parvozdan oldin:  12 266 UZS \nā¶  Parvozdan keyin: 36 798 UZS\
		\nToshkent - Istanbul:\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 367 980 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=ist_eko_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Rim\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  08:30  /  \nš¬ Qo'nish vaqti  --  12:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Bagaj: mavjud emas  ā\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nmavjud emas  ā\
		\n\nUzairplus - 3638 ball\
		\nChipta narxi - 4 814 571 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_nat_3kun_knopka)

@dp.callback_query_handler(text="rim_eko_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 135 990  UZS\
		\n\nš  Avaichiptani qaytarish \nRuxsat etilmaydi   ā\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko)

#5 kunlik tarif
@dp.callback_query_handler(text="rim_eko_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Rim\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  08:30  /  \nš¬ Qo'nish vaqti  --  12:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Bagaj: mavjud emas  ā\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nmavjud emas  ā\
		\n\nUzairplus - 3890 ball\
		\nChipta narxi - 4 990 500 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_nat_5kun_knopka)

@dp.callback_query_handler(text="rim_eko_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS  UZS\nā¶  Parvozdan keyin: 136 800 UZS\
		\n\nš  Avaichiptani qaytarish: \nRuxsat etilmaydi   ā\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko)

#7 kunlik tarif
@dp.callback_query_handler(text="rim_eko_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Rim\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  08:30  /  \nš¬ Qo'nish vaqti  --  12:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Bagaj: mavjud emas  ā\
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nmavjud emas  ā\
		\n\nUzairplus - 3890 ball\
		\nChipta narxi - 4 769 880 UZS\nTarif:  <ins>ekonom</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_nat_7kun_knopka)

@dp.callback_query_handler(text="rim_eko_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS  so'm\nā¶  Parvozdan keyin: 183 990 UZS so'm\
		\n\nš  Avaichiptani qaytarish: \nRuxsat etilmaydi   ā\
		\nā  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Rim\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  08:30  /  \nš¬ Qo'nish vaqti  --  12:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 3890 ball\
		\nChipta narxi - 8 516 763 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="rim_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko_plus)

#5 kunlik tarif
@dp.callback_query_handler(text="rim_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Rim\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  08:30  /  \nš¬ Qo'nish vaqti  --  12:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 3638 ball\
		\nChipta narxi - 8 616 800 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="rim_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_rim_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=rim_vaqt_eko_plus)

#7 kunlik tarif
@dp.callback_query_handler(text="rim_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Rim\
		\nāļø  Samolyot modeli  --  Airbus  320  Neo\
		\nš«  Uchib Ketish vaqti  --  08:30  /  \nš¬ Qo'nish vaqti  --  12:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \nā¶ļø  Maksimal hajmi: 158sm \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus - 3890 ball\
		\nChipta narxi - 8 450 800 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=rim_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="rim_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=rim_eko_plus_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - Dubay\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 08:25    \nš¬ Qo'nish vaqti  --  11:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 40kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  4950 ball\
		\nChipta narxi - 12 535 865 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="baa_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=baa_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_baa_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_biz)


#5 kunlik tarif biznes
@dp.callback_query_handler(text="baa_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Dubay\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 08:25    \nš¬ Qo'nish vaqti  --  11:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 40kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  4950 ball\
		\nChipta narxi - 11 835 876 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="baa_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=baa_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_baa_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_biz)


#7 kunlik tarif biznes

@dp.callback_query_handler(text="baa_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Dubay\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 08:25    \nš¬ Qo'nish vaqti  --  11:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 40kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  4950 ball\
		\nChipta narxi - 13 050 000 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="baa_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=baa_biz_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_baa_xalqaro_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_biz)



#3 kunlik tarif ekonom plus
@dp.callback_query_handler(text="vaqt_eko_plus_baa")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=baa_vaqt_eko_plus)

@dp.callback_query_handler(text="baa_eko_plus_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Dubay\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 08:25    \nš¬ Qo'nish vaqti  --  11:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 30kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  3300 ball\
		\nChipta narxi - 4 581 895 UZS\nTarif:  <ins>ekonom  +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="baa_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=baa_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_baa_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_eko_plus)

#5 kunlik tarif
@dp.callback_query_handler(text="baa_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Dubay\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 08:25    \nš¬ Qo'nish vaqti  --  11:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 30kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  3500 ball\
		\nChipta narxi - 5 220 830 UZS\nTarif:  <ins>ekonom  +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="baa_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=baa_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_baa_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=baa_vaqt_eko_plus)

#7 kunlik tarif
@dp.callback_query_handler(text="baa_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - Dubay\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 09:25    \nš¬ Qo'nish vaqti  --  12:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 30kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  3700 ball\
		\nChipta narxi - 4 990 830 UZS\nTarif:  <ins>ekonom  +</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=baa_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="baa_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=baa_eko_plus_nat_7kun_roziman)

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
	await call.message.answer("š  Yo'nalish:  Toshkent - London\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 10:45    \nš¬ Qo'nish vaqti  --  14:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  7893 ball\
		\nChipta narxi - 10 956 874 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_biz_nat_3kun_knopka)

@dp.callback_query_handler(text="bb_biz_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=bb_biz_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_bb_xalqaro_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_biz)


#5 kunlik tarif biznes
@dp.callback_query_handler(text="bb_biz_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - London\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 10:45    \nš¬ Qo'nish vaqti  --  14:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  7900 ball\
		\nChipta narxi - 11 156 574 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_biz_nat_5kun_knopka)

@dp.callback_query_handler(text="bb_biz_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=bb_biz_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_bb_xalqaro_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_biz)


#7 kunlik tarif biznes

@dp.callback_query_handler(text="bb_biz_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - London\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 10:45    \nš¬ Qo'nish vaqti  --  14:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 10kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 32kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  8392 ball\
		\nChipta narxi - 12 000 500 UZS\nTarif:  <ins>biznes</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_biz_nat_7kun_knopka)

@dp.callback_query_handler(text="bb_biz_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  122 660 UZS \nā¶  Parvozdan keyin: 183 990 UZS\
		\n\nš  Avaichiptani qaytarish  613 300 UZS  so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=bb_biz_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_bb_xalqaro_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_biz)



#3 kunlik tarif ekonom plus
@dp.callback_query_handler(text="vaqt_eko_plus_bb")
async def far_biz_vaqt(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ? ", reply_markup=bb_vaqt_eko_plus)

@dp.callback_query_handler(text="bb_eko_plus_nat_3")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - London\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 10:45    \nš¬ Qo'nish vaqti  --  14:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  5200 ball\
		\nChipta narxi - 7 892 592 UZS\nTarif:  <ins>ekonom  +</ins>\
		\nUchib ketish muddati:  <ins>3 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_eko_plus_nat_3kun_knopka)

@dp.callback_query_handler(text="bb_eko_plus_nat_3kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=bb_eko_plus_nat_3kun_roziman)

@dp.callback_query_handler(text="ort_bb_eko_plus_3kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_eko_plus)

#5 kunlik tarif eko plus
@dp.callback_query_handler(text="bb_eko_plus_nat_5")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - London\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 10:45    \nš¬ Qo'nish vaqti  --  14:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  5200 ball\
		\nChipta narxi - 7 892 592 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>5 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_eko_plus_nat_5kun_knopka)

@dp.callback_query_handler(text="bb_eko_plus_nat_5kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=bb_eko_plus_nat_5kun_roziman)

@dp.callback_query_handler(text="ort_bb_eko_plus_5kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_eko_plus)

#7 kunlik tarif eko plus
@dp.callback_query_handler(text="bb_eko_plus_nat_7")
async def far_vaqt_biz_nat(call:CallbackQuery):
	await call.message.answer("š  Yo'nalish:  Toshkent - London\
		\nāļø  Samolyot modeli  --  Airbus  320 Neo\
		\nš«  Uchib Ketish vaqti: 10:45    \nš¬ Qo'nish vaqti  --  14:00\
		\n\nšāļø  Qo'l yuki uchun qo'yilgan talablar  \nā¶ļø  Maksimal vazni: 8kg \
		\nš§³ā  Maksimal bagaj sig'imi \nā¶ļø  Maksimal vazni: 23kg \
		\n\nChiptani qayta rasmiylashtirish imkoniyati: \nMavjud  ā\
		\nChiptani qaytarish imkoniyati: \nMavjud  ā\
		\n\nUzairplus -  5200 ball\
		\nChipta narxi - 8 127 430 UZS\nTarif:  <ins>ekonom +</ins>\
		\nUchib ketish muddati:  <ins>7 kun ichida</ins>",parse_mode='HTML', reply_markup=bb_eko_plus_nat_7kun_knopka)

@dp.callback_query_handler(text="bb_eko_plus_nat_7kun_jarima")
async def far_biz_jar(call:CallbackQuery):
	await call.message.answer("š  š  Aviachiptani qayta rasmiylashtirish\
		\nā¶  Parvozdan oldin:  245 320 UZS \nā¶  Parvozdan keyin: 227 980 UZS\
		\n\nš  Avaichiptani qaytarish 520 300 UZS so'm\nā  Parvozga bir soat oldin kelmaslik", reply_markup=bb_eko_plus_nat_7kun_roziman)

@dp.callback_query_handler(text="ort_bb_eko_plus_7kun")
async def far_biz_vaqt_ortga(call:CallbackQuery):
	await call.message.answer("Necha kun ichida uchib ketasiz ?", reply_markup=bb_vaqt_eko_plus)


@dp.message_handler(text="Ortga     ā¤“ļø")
async def ortga_tarif(message:types. Message):
	await message.reply("Tarifni tanlang", reply_markup=xalqaro)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
