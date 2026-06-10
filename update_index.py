import sys

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if "<link href=\"https://fonts.googleapis.com/css2?family=Outfit" in line:
        new_lines.append(line)
        new_lines.append('    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital@0;1&display=swap" rel="stylesheet">\n')
        continue
        
    if "body {" in line and "font-family: 'Outfit', sans-serif;" in lines[i+1]:
        css = """
        /* Glowora Banner Styles */
        .hero-bg {
            background-image: url('hero_bg_generated.png');
            background-size: cover;
            background-position: center;
            height: 100vh;
            width: 100%;
            position: relative;
        }
        .hero-overlay {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(to right, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.3) 40%, rgba(0,0,0,0.1) 100%);
            z-index: 1;
        }
        .hero-content {
            position: relative;
            z-index: 2;
            height: 100%;
            display: flex;
            flex-direction: column;
            font-family: 'Inter', sans-serif;
        }
        .italic-serif {
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-weight: 400;
        }
"""
        new_lines.append(css + line)
        continue

    if "<!-- ==========================================" in line and i+1 < len(lines) and "NAVIGATION" in lines[i+1]:
        skip = True
        
        # Add the new Hero HTML
        new_lines.append("""    <!-- ==========================================
         HERO BANNER & NAVIGATION
         ========================================== -->
    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu"
        class="fixed inset-0 bg-brand-dark z-[2000] transform translate-x-full transition-transform duration-300 lg:hidden">
        <div class="p-8 flex flex-col h-full">
            <div class="flex justify-between items-center mb-16">
                <img src="aastralogo.png" alt="Aastra Aesthetic" class="h-10 w-auto brightness-0 invert">
                <button id="menu-close" class="text-white">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12">
                        </path>
                    </svg>
                </button>
            </div>
            <div class="flex flex-col gap-8 text-white text-xl font-bold tracking-widest uppercase">
                <a href="index.html">HOME</a>
                <a href="about.html">ABOUT</a>
                <a href="products.html">PRODUCT</a>
                <a href="services.html">SERVICES</a>
                <a href="contact.html">CONTACT</a>
                <a href="blog.html">BLOG</a>
            </div>
            <div class="mt-auto">
                <a href="contact.html"
                    class="btn-shimmer block bg-brand-primary text-white text-center py-5 text-sm font-bold tracking-[0.2em]">APPOINTMENT</a>
            </div>
        </div>
    </div>

    <!-- GLOWORA HERO BANNER (Modified for Aastra Aesthetic) -->
    <div class="hero-bg">
        <div class="hero-overlay"></div>
        <div class="hero-content px-8 md:px-16 py-8">
            <!-- Nav -->
            <nav class="flex justify-between items-center w-full relative z-[1000]">
                <div class="hidden md:flex gap-8 text-[13px] font-medium text-white/80">
                    <a href="index.html" class="hover:text-white transition">Home</a>
                    <a href="about.html" class="hover:text-white transition">About Us</a>
                    <a href="products.html" class="hover:text-white transition">Product</a>
                    <a href="services.html" class="hover:text-white transition">Service</a>
                </div>
                <div class="absolute left-1/2 transform -translate-x-1/2">
                    <a href="index.html">
                        <img src="aastralogo.png" alt="Aastra Aesthetic" class="h-12 md:h-16 w-auto brightness-0 invert opacity-90 object-contain">
                    </a>
                </div>
                <div class="flex items-center gap-6 text-[13px] font-medium text-white">
                    <a href="#" class="hover:text-white text-white/80 transition hidden sm:block">Log in</a>
                    <button class="px-6 py-2.5 rounded-full bg-white/20 hover:bg-white/30 backdrop-blur-md border border-white/10 transition hidden sm:block">Sign up</button>
                    <!-- Mobile Menu Toggle -->
                    <button id="menu-toggle" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center hover:bg-white/30 backdrop-blur-md transition text-white lg:hidden">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="4" y1="8" x2="20" y2="8"></line>
                            <line x1="4" y1="16" x2="20" y2="16"></line>
                        </svg>
                    </button>
                </div>
            </nav>

            <!-- Main Content -->
            <div class="flex-1 flex flex-col justify-center items-center text-center mt-8 text-white relative z-10 w-full h-full">
                <h1 class="text-4xl md:text-5xl lg:text-7xl font-bold leading-[1.2] tracking-tight mb-8">
                    AASTRA AESTHETIC <br class="hidden md:block">
                    <span class="italic-serif text-white/90 inline-block transition-all duration-500 transform opacity-100 translate-y-0" id="dynamic-hero-text">COSMETOLOGY & SKINCARE</span>
                </h1>
            </div>

            <!-- Testimonial -->
            <div class="absolute bottom-12 right-8 md:right-16 max-w-[320px] flex flex-col items-end hidden sm:flex text-white z-10">
                <div class="flex items-center gap-3 mb-5 mr-12">
                    <img src="https://i.pravatar.cc/100?img=5" class="w-10 h-10 rounded-full border border-white/20 object-cover" alt="Liya Anderson">
                    <div class="text-left">
                        <div class="text-sm font-medium text-white">Liya Anderson</div>
                        <div class="text-[11px] text-white/50 font-light mt-0.5">CEO of Clarity</div>
                    </div>
                </div>
                
                <div class="flex items-center gap-4 mb-4 w-full">
                    <button class="w-7 h-7 rounded-full bg-white/10 backdrop-blur-sm border border-white/10 flex items-center justify-center hover:bg-white/20 shrink-0 text-white/50 transition">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                    </button>
                    <div class="h-[2px] bg-white/20 flex-1 relative rounded-full">
                        <div class="absolute top-0 left-0 h-full bg-white/80 w-1/3 rounded-full"></div>
                    </div>
                    <button class="w-7 h-7 rounded-full bg-white/10 backdrop-blur-sm border border-white/10 flex items-center justify-center hover:bg-white/20 shrink-0 text-white transition">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
                    </button>
                </div>
                
                <p class="text-[12px] text-white/70 leading-[1.6] text-right font-light">
                    I purchased from Glowora and the experience was fantastic. Their products are high quality, gentle on the skin, and delivered on time.
                </p>
            </div>
        </div>
    </div>\n""")
        continue

    if skip and "<!-- ==========================================" in line and i+1 < len(lines) and "BOOKING BAR" in lines[i+1]:
        skip = False

    if not skip:
        new_lines.append(line)

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("index.html updated successfully!")
