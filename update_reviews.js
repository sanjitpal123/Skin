const fs = require('fs');

let content = fs.readFileSync('landing.html', 'utf8');

// Review 1
content = content.replace(/Priya Sharma/g, "Syed Aamir usman");
content = content.replace(/6 months ago/g, "4 months ago");
content = content.replace(/>P</g, ">S<");
content = content.replace(/Melasma Treatment/g, "Aesthetic Treatments");
content = content.replace(/"I had severe melasma patches for years[\s\S]*?enough!"/g, '"Aastra Aesthetic is an excellent clinic with a very clean and calming environment. The staff is polite, professional, and makes you feel comfortable from the first visit. Ms.sania explains every procedure clearly and treats patients with genuine care. Results are satisfying and the overall experience is smooth and trustworthy. Highly recommended for anyone looking for quality aesthetic treatments."');

// Review 2
content = content.replace(/Ananya Reddy/g, "Uzma Ali");
content = content.replace(/3 months ago/g, "4 weeks ago");
content = content.replace(/>A</g, ">U<");
content = content.replace(/Scar Treatment/g, "Cosmetology");
content = content.replace(/"My acne scars have reduced by 80%[\s\S]*?Best Cosmetologist!"/g, '"Excellent service,good behaviour of staff and very professional 😊 Cosmetologist is also very cooperative and understands customer\'s needs."');

// Review 3
content = content.replace(/Rahul Verma/g, "Amir Hamza");
content = content.replace(/2 months ago/g, "a month ago");
content = content.replace(/>R</g, ">A<");
content = content.replace(/Hair Fall/g, "Acne Treatment");
content = content.replace(/"My hair fall reduced dramatically[\s\S]*?Truly grateful!"/g, '"I am currently undergoing treatment at Aastra Aesthetic Clinic, and the results so far have been very good. My pimples have reduced significantly, and my skin is glowing much more now. Sania Ma’am and all the staff have a very good and polite behavior. They guide you properly and take great care. I would definitely recommend everyone to visit the clinic."');

// Review 4
content = content.replace(/Meera Kapoor/g, "Shaina Hussain");
content = content.replace(/1 month ago/g, "a month ago");
content = content.replace(/>M</g, ">S<");
content = content.replace(/Face Lifting/g, "Aesthetic Care");
content = content.replace(/"The HIFU face lifting treatment[\s\S]*?comfortable."/g, '"Excellent service! So helpful and kind Extremely co- operative and understanding staff Moreover it’s hygienic and well maintained Wonderful experience.🥰"');

// Review 5
content = content.replace(/Sneha Patel/g, "Shazz Khan");
content = content.replace(/2 weeks ago/g, "a month ago");
content = content.replace(/Skin Rejuvenation/g, "Skin Glowing & IV Drip");
content = content.replace(/"Got the HydraFacial for my wedding prep[\s\S]*?(?:ðŸ’•|💕)"/g, '"Wonderful Ambience , Experienced & Polite Staffs with cleanliness in every aspects. I have done my Skin glowing treatment and it has work wonders on my face apart from that now i am taking gluthatione iv drip sessions and it is slowly slowly showing good effect on my skin and from my personal experience i must suggest it for all of you irrespective of genders.🙌🏻💯"');

// Fallback for Review 5 if exact matching fails due to encoding
if (!content.includes("Wonderful Ambience")) {
    content = content.replace(/"Got the HydraFacial for my wedding prep[\s\S]*?"/g, '"Wonderful Ambience , Experienced & Polite Staffs with cleanliness in every aspects. I have done my Skin glowing treatment and it has work wonders on my face apart from that now i am taking gluthatione iv drip sessions and it is slowly slowly showing good effect on my skin and from my personal experience i must suggest it for all of you irrespective of genders.🙌🏻💯"');
}

fs.writeFileSync('landing.html', content, 'utf8');
console.log('Reviews updated successfully.');
