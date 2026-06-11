$content = Get-Content 'landing.html' -Raw

$content = $content -replace '(?s)"I had severe melasma patches for years.*?enough!"', '"Aastra Aesthetic is an excellent clinic with a very clean and calming environment. The staff is polite, professional, and makes you feel comfortable from the first visit. Ms.sania explains every procedure clearly and treats patients with genuine care. Results are satisfying and the overall experience is smooth and trustworthy. Highly recommended for anyone looking for quality aesthetic treatments."'
$content = $content -replace 'Priya Sharma', 'Syed Aamir usman'
$content = $content -replace '6 months ago', '4 months ago'
$content = $content -replace '>P<', '>S<'
$content = $content -replace 'Melasma Treatment', 'Aesthetic Treatments'

$content = $content -replace '(?s)"My acne scars have reduced by 80%.*?Best Cosmetologist!"', '"Excellent service,good behaviour of staff and very professional 😊 Cosmetologist is also very cooperative and understands customer''s needs."'
$content = $content -replace 'Ananya Reddy', 'Uzma Ali'
$content = $content -replace '3 months ago', '4 weeks ago'
$content = $content -replace '>A<', '>U<'
$content = $content -replace 'Scar Treatment', 'Cosmetology'

$content = $content -replace '(?s)"My hair fall reduced dramatically.*?Truly grateful!"', '"I am currently undergoing treatment at Aastra Aesthetic Clinic, and the results so far have been very good. My pimples have reduced significantly, and my skin is glowing much more now. Sania Ma’am and all the staff have a very good and polite behavior. They guide you properly and take great care. I would definitely recommend everyone to visit the clinic."'
$content = $content -replace 'Rahul Verma', 'Amir Hamza'
$content = $content -replace '2 months ago', 'a month ago'
$content = $content -replace '>R<', '>A<'
$content = $content -replace 'Hair Fall', 'Acne Treatment'

$content = $content -replace '(?s)"The HIFU face lifting treatment.*?comfortable."', '"Excellent service! So helpful and kind Extremely co- operative and understanding staff Moreover it’s hygienic and well maintained Wonderful experience.🥰"'
$content = $content -replace 'Meera Kapoor', 'Shaina Hussain'
$content = $content -replace '1 month ago', 'a month ago'
$content = $content -replace '>M<', '>S<'
$content = $content -replace 'Face Lifting', 'Aesthetic Care'

$content = $content -replace '(?s)"Got the HydraFacial for my wedding prep.*?"', '"Wonderful Ambience , Experienced & Polite Staffs with cleanliness in every aspects. I have done my Skin glowing treatment and it has work wonders on my face apart from that now i am taking gluthatione iv drip sessions and it is slowly slowly showing good effect on my skin and from my personal experience i must suggest it for all of you irrespective of genders.🙌🏻💯"'
$content = $content -replace 'Sneha Patel', 'Shazz Khan'
$content = $content -replace '2 weeks ago', 'a month ago'
$content = $content -replace 'Skin Rejuvenation', 'Skin Glowing & IV Drip'

Set-Content -Path 'landing.html' -Value $content -Encoding UTF8
