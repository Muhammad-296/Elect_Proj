<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CMOS Logic Analyzer - Professional README</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Fira+Code:wght@400;500&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
            color: #333;
            line-height: 1.8;
            overflow-x: hidden;
        }

        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            animation: float 20s infinite;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) translateX(0);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) translateX(100px);
                opacity: 0;
            }
        }

        .container {
            max-width: 1400px;
            margin: 40px auto;
            background: white;
            border-radius: 30px;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.4);
            overflow: hidden;
            position: relative;
            z-index: 1;
            animation: containerFadeIn 1.5s cubic-bezier(0.22, 1, 0.36, 1);
        }

        @keyframes containerFadeIn {
            from {
                opacity: 0;
                transform: translateY(60px) scale(0.95);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            color: white;
            padding: 80px 60px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: repeating-linear-gradient(
                45deg,
                transparent,
                transparent 20px,
                rgba(255, 255, 255, 0.03) 20px,
                rgba(255, 255, 255, 0.03) 40px
            );
            animation: moveStripes 20s linear infinite;
        }

        @keyframes moveStripes {
            0% {
                transform: translate(0, 0);
            }
            100% {
                transform: translate(50px, 50px);
            }
        }

        .logo {
            font-size: 80px;
            margin-bottom: 20px;
            animation: logoFloat 3s ease-in-out infinite;
            display: inline-block;
            position: relative;
            z-index: 2;
            filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.3));
        }

        @keyframes logoFloat {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            50% {
                transform: translateY(-20px) rotate(5deg);
            }
        }

        h1 {
            font-size: 4em;
            font-weight: 700;
            margin-bottom: 15px;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
            animation: titleSlideDown 1s cubic-bezier(0.22, 1, 0.36, 1);
            position: relative;
            z-index: 2;
            letter-spacing: 2px;
        }

        @keyframes titleSlideDown {
            from {
                opacity: 0;
                transform: translateY(-80px) scale(0.8);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        .subtitle {
            font-size: 1.5em;
            opacity: 0.95;
            animation: subtitleSlideUp 1s cubic-bezier(0.22, 1, 0.36, 1) 0.3s both;
            position: relative;
            z-index: 2;
            font-weight: 300;
            letter-spacing: 1px;
        }

        @keyframes subtitleSlideUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }
            to {
                opacity: 0.95;
                transform: translateY(0);
            }
        }

        .badges {
            margin-top: 30px;
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
            position: relative;
            z-index: 2;
        }

        .badge {
            background: rgba(255, 255, 255, 0.25);
            padding: 12px 24px;
            border-radius: 30px;
            font-size: 0.95em;
            font-weight: 600;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.4);
            animation: badgePop 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55) backwards;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .badge:nth-child(1) { animation-delay: 0.5s; }
        .badge:nth-child(2) { animation-delay: 0.6s; }
        .badge:nth-child(3) { animation-delay: 0.7s; }
        .badge:nth-child(4) { animation-delay: 0.8s; }

        @keyframes badgePop {
            0% {
                opacity: 0;
                transform: scale(0) rotate(-180deg);
            }
            100% {
                opacity: 1;
                transform: scale(1) rotate(0deg);
            }
        }

        .badge:hover {
            transform: translateY(-5px) scale(1.1);
            background: rgba(255, 255, 255, 0.35);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .nav-links {
            margin-top: 35px;
            display: flex;
            justify-content: center;
            gap: 25px;
            flex-wrap: wrap;
            position: relative;
            z-index: 2;
        }

        .nav-link {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border: 2px solid rgba(255, 255, 255, 0.5);
            border-radius: 25px;
            transition: all 0.3s ease;
            font-weight: 500;
            animation: navLinkFade 0.8s ease backwards;
        }

        .nav-link:nth-child(1) { animation-delay: 0.9s; }
        .nav-link:nth-child(2) { animation-delay: 1.0s; }
        .nav-link:nth-child(3) { animation-delay: 1.1s; }
        .nav-link:nth-child(4) { animation-delay: 1.2s; }
        .nav-link:nth-child(5) { animation-delay: 1.3s; }

        @keyframes navLinkFade {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .nav-link:hover {
            background: white;
            color: #667eea;
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }

        .content {
            padding: 60px;
        }

        .section {
            margin-bottom: 60px;
            opacity: 0;
            animation: sectionFadeIn 1s ease forwards;
        }

        @keyframes sectionFadeIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .section:nth-child(1) { animation-delay: 0.1s; }
        .section:nth-child(2) { animation-delay: 0.2s; }
        .section:nth-child(3) { animation-delay: 0.3s; }
        .section:nth-child(4) { animation-delay: 0.4s; }
        .section:nth-child(5) { animation-delay: 0.5s; }

        h2 {
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 4px solid transparent;
            background: linear-gradient(to right, #667eea 0%, #764ba2 100%);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            font-weight: 700;
        }

        h2::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 4px;
            background: linear-gradient(to right, #667eea, #764ba2);
            animation: expandUnderline 1.5s ease forwards;
        }

        @keyframes expandUnderline {
            to {
                width: 100%;
            }
        }

        h3 {
            color: #764ba2;
            font-size: 1.8em;
            margin: 30px 0 15px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .info-highlight {
            background: linear-gradient(135deg, #667eea15 0%, #764ba225 100%);
            border-left: 5px solid #667eea;
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
            animation: slideInLeft 0.8s ease;
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.1);
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }

        .feature-card {
            background: linear-gradient(135deg, #ffffff 0%, #f5f7fa 100%);
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
            animation: cardScale 0.6s ease backwards;
        }

        .feature-card:nth-child(1) { animation-delay: 0.1s; }
        .feature-card:nth-child(2) { animation-delay: 0.2s; }
        .feature-card:nth-child(3) { animation-delay: 0.3s; }
        .feature-card:nth-child(4) { animation-delay: 0.4s; }
        .feature-card:nth-child(5) { animation-delay: 0.5s; }
        .feature-card:nth-child(6) { animation-delay: 0.6s; }

        @keyframes cardScale {
            from {
                opacity: 0;
                transform: scale(0.8) rotateY(-15deg);
            }
            to {
                opacity: 1;
                transform: scale(1) rotateY(0deg);
            }
        }

        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: 0;
        }

        .feature-card:hover::before {
            opacity: 0.05;
        }

        .feature-card:hover {
            transform: translateY(-15px) scale(1.05);
            box-shadow: 0 20px 50px rgba(102, 126, 234, 0.3);
            border: 2px solid #667eea;
        }

        .feature-icon {
            font-size: 3.5em;
            margin-bottom: 20px;
            display: block;
            position: relative;
            z-index: 1;
            transition: all 0.4s ease;
        }

        .feature-card:hover .feature-icon {
            animation: iconBounce 0.8s ease;
            transform: scale(1.2);
        }

        @keyframes iconBounce {
            0%, 100% {
                transform: translateY(0) scale(1.2);
            }
            25% {
                transform: translateY(-15px) scale(1.2) rotate(-5deg);
            }
            50% {
                transform: translateY(-25px) scale(1.2) rotate(5deg);
            }
            75% {
                transform: translateY(-15px) scale(1.2) rotate(-3deg);
            }
        }

        .feature-title {
            font-weight: 700;
            color: #667eea;
            font-size: 1.4em;
            margin-bottom: 15px;
            position: relative;
            z-index: 1;
        }

        .feature-description {
            color: #666;
            line-height: 1.6;
            position: relative;
            z-index: 1;
        }

        .tech-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 30px 0;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            border-radius: 15px;
            overflow: hidden;
            animation: tableSlideUp 1s ease;
        }

        @keyframes tableSlideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .tech-table thead {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .tech-table th {
            padding: 20px;
            text-align: left;
            font-weight: 600;
            font-size: 1.1em;
            letter-spacing: 0.5px;
        }

        .tech-table td {
            padding: 18px 20px;
            border-bottom: 1px solid #e0e0e0;
            transition: all 0.3s ease;
        }

        .tech-table tbody tr {
            transition: all 0.3s ease;
            background: white;
        }

        .tech-table tbody tr:hover {
            background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%);
            transform: scale(1.02);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
        }

        .code-block {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 30px;
            border-radius: 15px;
            overflow-x: auto;
            margin: 25px 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            font-family: 'Fira Code', monospace;
            font-size: 0.95em;
            line-height: 1.6;
            position: relative;
            animation: codeSlideIn 1s ease;
        }

        @keyframes codeSlideIn {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .code-block::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(to right, #667eea, #764ba2, #f093fb);
        }

        .code-block pre {
            margin: 0;
        }

        .code-keyword {
            color: #569cd6;
        }

        .code-string {
            color: #ce9178;
        }

        .code-comment {
            color: #6a9955;
            font-style: italic;
        }

        .formula-box {
            background: linear-gradient(135deg, #fff5f5 0%, #ffe0e0 100%);
            padding: 30px;
            border-radius: 15px;
            margin: 25px 0;
            border-left: 6px solid #ff6b6b;
            box-shadow: 0 5px 20px rgba(255, 107, 107, 0.2);
            animation: formulaSlideIn 0.8s ease;
            position: relative;
            overflow: hidden;
        }

        @keyframes formulaSlideIn {
            from {
                opacity: 0;
                transform: translateX(-50px) rotateY(-10deg);
            }
            to {
                opacity: 1;
                transform: translateX(0) rotateY(0deg);
            }
        }

        .formula-box::before {
            content: '∫';
            position: absolute;
            top: -20px;
            right: -20px;
            font-size: 150px;
            opacity: 0.05;
            font-weight: bold;
        }

        .formula-title {
            font-size: 1.3em;
            font-weight: 700;
            color: #ff6b6b;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .formula-content {
            font-family: 'Fira Code', monospace;
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            font-size: 0.95em;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .install-steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin: 30px 0;
        }

        .install-step {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0, 188, 212, 0.2);
            transition: all 0.3s ease;
            animation: stepPop 0.6s ease backwards;
        }

        .install-step:nth-child(1) { animation-delay: 0.1s; }
        .install-step:nth-child(2) { animation-delay: 0.2s; }
        .install-step:nth-child(3) { animation-delay: 0.3s; }

        @keyframes stepPop {
            from {
                opacity: 0;
                transform: scale(0.5);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        .install-step:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0, 188, 212, 0.3);
        }

        .step-number {
            display: inline-block;
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #00bcd4, #0097a7);
            color: white;
            border-radius: 50%;
            text-align: center;
            line-height: 40px;
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 15px;
            box-shadow: 0 5px 15px rgba(0, 188, 212, 0.4);
        }

        .step-title {
            font-weight: 700;
            color: #00838f;
            font-size: 1.2em;
            margin-bottom: 10px;
        }

        .criteria-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .criteria-card {
            background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(255, 235, 59, 0.3);
            transition: all 0.4s ease;
            animation: criteriaFlip 0.8s ease backwards;
        }

        .criteria-card:nth-child(1) { animation-delay: 0.1s; }
        .criteria-card:nth-child(2) { animation-delay: 0.2s; }
        .criteria-card:nth-child(3) { animation-delay: 0.3s; }
        .criteria-card:nth-child(4) { animation-delay: 0.4s; }

        @keyframes criteriaFlip {
            from {
                opacity: 0;
                transform: rotateY(-90deg);
            }
            to {
                opacity: 1;
                transform: rotateY(0deg);
            }
        }

        .criteria-card:hover {
            transform: scale(1.1) rotate(2deg);
            box-shadow: 0 15px 40px rgba(255, 235, 59, 0.5);
        }

        .criteria-icon {
            font-size: 3em;
            margin-bottom: 15px;
            display: block;
            animation: criteriaIconSpin 3s linear infinite;
        }

        @keyframes criteriaIconSpin {
            0%, 90%, 100% {
                transform: rotate(0deg);
            }
            95% {
                transform: rotate(360deg);
            }
        }

        .criteria-card:hover .criteria-icon {
            animation: criteriaIconBounce 0.6s ease;
        }

        @keyframes criteriaIconBounce {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.3);
            }
        }

        .criteria-label {
            font-weight: 700;
            color: #f57f17;
            font-size: 1.1em;
        }

        .footer {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 50px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .footer::before {
            content: '';
            position: absolute;
            top: -2px;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(to right, #667eea, #764ba2, #f093fb);
        }

        .footer-content {
            position: relative;
            z-index: 1;
        }

        .footer h3 {
            color: white;
            margin-bottom: 20px;
            font-size: 1.8em;
        }

        .footer a {
            color: #667eea;
            text-decoration: none;
            transition: all 0.3s ease;
            font-weight: 600;
        }

        .footer a:hover {
            color: #f093fb;
            text-decoration: underline;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }

        .social-icon {
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5em;
            transition: all 0.3s ease;
            cursor: pointer;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }

        .social-icon:hover {
            background: white;
            color: #667eea;
            transform: translateY(-5px) rotate(360deg);
            box-shadow: 0 10px 30px rgba(255, 255, 255, 0.3);
        }

        .highlight {
            background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
            padding: 4px 10px;
            border-radius: 8px;
            font-weight: 700;
            color: #1e3c72;
        }

        ul {
            list-style: none;
            padding-left: 0;
        }

        li {
            padding: 12px 0;
            padding-left: 35px;
            position: relative;
            transition: all 0.3s ease;
        }

        li::before {
            content: '▶';
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
            font-size: 0.8em;
            transition: all 0.3s ease;
        }

        li:hover {
            padding-left: 45px;
            color: #667eea;
        }

        li:hover::before {
            transform: translateX(5px);
        }

        .warning-box {
            background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
            border-left: 6px solid #fbc02d;
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
            box-shadow: 0 5px 20px rgba(251, 192, 45, 0.2);
            animation: warningPulse 2s ease-in-out infinite;
        }

        @keyframes warningPulse {
            0%, 100% {
                box-shadow: 0 5px 20px rgba(251, 192, 45, 0.2);
            }
            50% {
                box-shadow: 0 5px 30px rgba(251, 192, 45, 0.4);
            }
        }

        @media (max-width: 768px) {
            .container {
                margin: 20px;
                border-radius: 20px;
            }

            h1 {
                font-size: 2.5em;
            }

            .logo {
                font-size: 60px;
            }

            .content {
                padding: 30px;
            }

            .feature-grid {
                grid-template-columns: 1fr;
            }

            .tech-table {
                font-size: 0.85em;
            }

            .tech-table th,
            .tech-table td {
                padding: 12px;
            }
        }

        .scroll-indicator {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5em;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            transition: all 0.3s ease;
            z-index: 1000;
            animation: scrollBounce 2s ease-in-out infinite;
        }

        @keyframes scrollBounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        .scroll-indicator:hover {
            transform: scale(1.1);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
        }
    </style>
</head>
<body>
    <!-- Particle Background -->
    <div class="particles" id="particles"></div>

    <!-- Scroll to Top Button -->
    <div class="scroll-indicator" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
        ↑
    </div>

    <div class="container">
        <!-- Header Section -->
        <div class="header">
            <div class="logo">⚡</div>
            <h1>CMOS Logic Analyzer</h1>
            <p class="subtitle">Advanced Digital Circuit Design & Performance Analysis Tool</p>
            <div class="badges">
                <span class="badge">🔬 Python 3.7+</span>
                <span class="badge">⚙️ CMOS Technology</span>
                <span class="badge">📊 Performance Analysis</span>
                <span class="badge">🎨 Colorful CLI</span>
            </div>
            <div class="nav-links">
                <a href="#features" class="nav-link">Features</a>
                <a href="#installation" class="nav-link">Installation</a>
                <a href="#usage" class="nav-link">Usage</a>
                <a href="#formulas" class="nav-link">Formulas</a>
                <a href="#contributing" class="nav-link">Contributing</a>
            </div>
        </div>

        <!-- Content Section -->
        <div class="content">
            <!-- Overview Section -->
            <div class="section" id="overview">
                <h2>📖 Overview</h2>
                <p style="font-size: 1.15em; line-height: 1.8;">A comprehensive Python-based tool for analyzing and optimizing CMOS logic circuits. This analyzer implements <strong>exact delay calculations</strong>, area optimization, and power analysis for digital logic designs using both NAND+NOT and NOR+NOT implementations.</p>
                
                <div class="info-highlight">
                    <strong style="font-size: 1.2em;">🎯 Key Highlight:</strong> This tool uses <span class="highlight">EXACT mathematical formulas</span> derived from MOSFET physics for delay, area, and power calculations—not approximations! Every calculation is based on fundamental semiconductor equations and technology-specific parameters.
                </div>
            </div>

            <!-- Features Section -->
            <div class="section" id="features">
                <h2>✨ Features</h2>
                <div class="feature-grid">
                    <div class="feature-card">
                        <span class="feature-icon">🔧</span>
                        <div class="feature-title">Logic Minimization</div>
                        <p class="feature-description">Implements Quine-McCluskey algorithm for optimal Boolean function simplification with beautiful K-map visualization and prime implicant grouping.</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">⚡</span>
                        <div class="feature-title">Exact Delay Calculation</div>
                        <p class="feature-description">Precise propagation delay using non-linear MOSFET equations, capacitance models, and separate rise/fall time analysis.</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">📐</span>
                        <div class="feature-title">Area Optimization</div>
                        <p class="feature-description">Exact area calculation using formula: n×Wn(ln+2LDn) + wp(lp+2LDp) with technology-dependent parameters.</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">🔋</span>
                        <div class="feature-title">Power Analysis</div>
                        <p class="feature-description">Maximum power dissipation calculation with switching voltage analysis and dynamic power estimation.</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">🎨</span>
                        <div class="feature-title">Visual K-Maps</div>
                        <p class="feature-description">Color-coded Karnaugh maps (2, 3, 4 variables) with prime implicant highlighting and interactive display.</p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">📊</span>
                        <div class="feature-title">Comparative Analysis</div>
                        <p class="feature-description">Side-by-side comparison of NAND+NOT vs NOR+NOT with 4-criteria optimization scoring and recommendation engine.</p>
                    </div>
                </div>
            </div>

            <!-- Technologies Section -->
            <div class="section" id="technologies">
                <h2>🔬 Supported CMOS Technologies</h2>
                <table class="tech-table">
                    <thead>
                        <tr>
                            <th>Technology</th>
                            <th>Gate Oxide</th>
                            <th>Vth (V)</th>
                            <th>μn (cm²/V·s)</th>
                            <th>μp (cm²/V·s)</th>
                            <th>Applications</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>1.0µm CMOS</strong></td>
                            <td>20 nm</td>
                            <td>±0.9</td>
                            <td>450</td>
                            <td>180</td>
                            <td>Legacy systems, education</td>
                        </tr>
                        <tr>
                            <td><strong>0.8µm CMOS</strong></td>
                            <td>16 nm</td>
                            <td>±0.8</td>
                            <td>460</td>
                            <td>185</td>
                            <td>Moderate performance</td>
                        </tr>
                        <tr>
                            <td><strong>0.6µm CMOS</strong></td>
                            <td>12 nm</td>
                            <td>±0.75</td>
                            <td>470</td>
                            <td>190</td>
                            <td>Standard digital logic</td>
                        </tr>
                        <tr>
                            <td><strong>0.5µm CMOS</strong></td>
                            <td>10 nm</td>
                            <td>±0.7</td>
                            <td>460</td>
                            <td>190</td>
                            <td>High-speed circuits</td>
                        </tr>
                        <tr>
                            <td><strong>0.35µm CMOS</strong></td>
                            <td>7 nm</td>
                            <td>±0.5</td>
                            <td>500</td>
                            <td>200</td>
                            <td>Advanced applications</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Installation Section -->
            <div class="section" id="installation">
                <h2>🚀 Installation</h2>
                <h3>📦 Prerequisites</h3>
                <div class="install-steps">
                    <div class="install-step">
                        <span class="step-number">1</span>
                        <div class="step-title">Python 3.7+</div>
                        <p>Ensure you have Python 3.7 or higher installed on your system</p>
                    </div>
                    <div class="install-step">
                        <span class="step-number">2</span>
                        <div class="step-title">Package Manager</div>
                        <p>pip should be installed and updated to the latest version</p>
                    </div>
                    <div class="install-step">
                        <span class="step-number">3</span>
                        <div class="step-title">Dependencies</div>
                        <p>Install colorama and tabulate packages</p>
                    </div>
                </div>

                <h3>💻 Installation Steps</h3>
                <div class="code-block">
<pre><span class="code-comment"># Clone the repository</span>
<span class="code-keyword">git clone</span> <span class="code-string">https://github.com/yourusername/cmos-logic-analyzer.git</span>

<span class="code-comment"># Navigate to project directory</span>
<span class="code-keyword">cd</span> cmos-logic-analyzer

<span class="code-comment"># Install dependencies</span>
<span class="code-keyword">pip install</span> <span class="code-string">colorama tabulate</span>

<span class="code-comment"># Run the analyzer</span>
<span class="code-keyword">python</span> main.py</pre>
                </div>
            </div>

            <!-- Usage Section -->
            <div class="section" id="usage">
                <h2>💡 Usage</h2>
                <p style="font-size: 1.1em;">Launch the interactive analyzer and follow the prompts:</p>
                <div class="code-block">
<pre><span class="code-keyword">python</span> main.py

<span class="code-comment"># Interactive prompts will guide you through:</span>
<span class="code-string">1. Technology selection (1.0µm to 0.35µm)</span>
<span class="code-string">2. MOSFET dimensions (Wn, Ln, Wp, Lp)</span>
<span class="code-string">3. Logic function input (minterms/maxterms)</span>
<span class="code-string">4. Automatic analysis and comparison</span>
<span class="code-string">5. Design recommendation</span></pre>
                </div>

                <div class="info-highlight">
                    <strong>📝 Example Input:</strong><br>
                    Technology: <code style="background: rgba(102,126,234,0.1); padding: 3px 8px; border-radius: 5px;">0.35µm CMOS</code><br>
                    Wn = 2.0µm, Ln = 0.35µm<br>
                    Wp = 4.0µm, Lp = 0.35µm<br>
                    Minterms: <code style="background: rgba(102,126,234,0.1); padding: 3px 8px; border-radius: 5px;">1, 3, 5, 7, 9, 11, 13, 15</code>
                </div>
            </div>

            <!-- Formulas Section -->
            <div class="section" id="formulas">
                <h2>🧮 Mathematical Formulas</h2>
                
                <div class="formula-box">
                    <div class="formula-title">📊 NOT Gate Delay</div>
                    <p><strong>Load Capacitance (VBS ≠ 0):</strong></p>
                    <div class="formula-content">
                        C<sub>load</sub> = n(C<sub>gd_pc</sub> + C<sub>gd_nt</sub> + C<sub>db_pt</sub>) + C<sub>db_nc</sub> + C<sub>gb_pc</sub>
                    </div>
                    <p style="margin-top: 15px;"><strong>Fall & Rise Delays:</strong></p>
                    <div class="formula-content">
                        Z<sub>NOT</sub><sup>-</sup> = R<sub>n</sub> × C<sub>load</sub><br>
                        Z<sub>NOT</sub><sup>+</sup> = R<sub>p</sub> × C<sub>load</sub>
                    </div>
                </div>

                <div class="formula-box">
                    <div class="formula-title">⚡ NAND Gate Delay</div>
                    <p><strong>Parameters:</strong></p>
                    <div class="formula-content">
                        a = V<sub>DD</sub> - V<sub>th_n</sub><br>
                        X₁ = a(1 - √(1/n))<br>
                        X₂ = a(1 - √(1/n [1 + (1 - V<sub>th_n</sub>/a)²(n-1)]))
                    </div>
                    <p style="margin-top: 15px;"><strong>Falling Edge Delay:</strong></p>
                    <div class="formula-content">
                        Z<sub>ND</sub><sup>-</sup> = (n × C<sub>load</sub><sup>-</sup> × 10⁶) / ((n² - 1)K<sub>n</sub> × a) × [logarithmic terms]
                    </div>
                </div>

                <div class="formula-box">
                    <div class="formula-title">🔄 NOR Gate Delay</div>
                    <p><strong>Parameters:</strong></p>
                    <div class="formula-content">
                        a = V<sub>DD</sub> - |V<sub>th_p</sub>|<br>
                        Similar structure to NAND with PMOS parameters
                    </div>
                    <p style="margin-top: 15px;"><strong>Rising Edge Delay:</strong></p>
                    <div class="formula-content">
                        Z<sub>NR</sub><sup>+</sup> = (n × C<sub>load</sub><sup>+</sup> × 10⁶) / ((n² - 1)K<sub>p</sub> × a) × [logarithmic terms]
                    </div>
                </div>

                <div class="formula-box">
                    <div class="formula-title">📐 Area Calculation</div>
                    <div class="formula-content">
                        Area = n×W<sub>n</sub>(l<sub>n</sub> + 2L<sub>Dn</sub>) + w<sub>p</sub>(l<sub>p</sub> + 2L<sub>Dp</sub>) [µm²]<br><br>
                        where n = number of inputs, W<sub>n</sub>, W<sub>p</sub> = widths, L<sub>Dn</sub>, L<sub>Dp</sub> = lateral diffusion lengths
                    </div>
                </div>

                <div class="formula-box">
                    <div class="formula-title">🔋 Maximum Power</div>
                    <div class="formula-content">
                        V<sub>inss</sub> = (√K<sub>n</sub> × V<sub>th_n</sub> + √K<sub>p</sub>(V<sub>DD</sub> - V<sub>th_p</sub>)) / (√K<sub>n</sub> + √K<sub>p</sub>)<br><br>
                        P<sub>max</sub> = G × (K<sub>n</sub>/2) × (V<sub>inss</sub> - V<sub>th_n</sub>)² × V<sub>DD</sub> [µW]
                    </div>
                </div>
            </div>

            <!-- Optimization Criteria -->
            <div class="section" id="optimization">
                <h2>🎯 Design Optimization Criteria</h2>
                <p style="font-size: 1.1em; margin-bottom: 20px;">The analyzer evaluates both implementations on four key metrics:</p>
                <div class="criteria-grid">
                    <div class="criteria-card">
                        <span class="criteria-icon">🏆</span>
                        <div class="criteria-label">Area</div>
                        <p>Minimizes silicon footprint (µm²)</p>
                    </div>
                    <div class="criteria-card">
                        <span class="criteria-icon">⚡</span>
                        <div class="criteria-label">Speed</div>
                        <p>Maximizes bit rate (MHz)</p>
                    </div>
                    <div class="criteria-card">
                        <span class="criteria-icon">🔋</span>
                        <div class="criteria-label">Power</div>
                        <p>Minimizes consumption (µW)</p>
                    </div>
                    <div class="criteria-card">
                        <span class="criteria-icon">🎚️</span>
                        <div class="criteria-label">Gates</div>
                        <p>Reduces complexity (count)</p>
                    </div>
                </div>
            </div>

            <!-- Technical Highlights -->
            <div class="section" id="highlights">
                <h2>🔍 Technical Highlights</h2>
                <ul style="font-size: 1.05em;">
                    <li><strong>Non-linear delay models:</strong> Exact logarithmic equations, not RC approximations</li>
                    <li><strong>Body effect consideration:</strong> Accurate V<sub>th</sub> calculation with V<sub>BS</sub> variations</li>
                    <li><strong>Capacitance extraction:</strong> Separate cutoff and triode region capacitances</li>
                    <li><strong>Load calculation:</strong> C<sub>gd</sub>, C<sub>gs</sub>, C<sub>db</sub>, C<sub>gb</sub> components for each transistor</li>
                    <li><strong>Multi-input support:</strong> 2-input to n-input NAND/NOR gates with exact formulas</li>
                    <li><strong>Technology scaling:</strong> Accurate parameters from 1.0µm down to 0.35µm processes</li>
                </ul>
            </div>

            <!-- Limitations -->
            <div class="section" id="limitations">
                <h2>⚠️ Limitations & Assumptions</h2>
                <div class="warning-box">
                    <strong style="font-size: 1.2em;">⚙️ Important Notes:</strong>
                    <ul style="margin-top: 15px; font-size: 1.05em;">
                        <li>Assumes ideal switching conditions (no noise)</li>
                        <li>Room temperature operation (T = 300K)</li>
                        <li>Fixed supply voltage (V<sub>DD</sub> = 5.0V)</li>
                        <li>Neglects interconnect parasitics (RC wiring)</li>
                        <li>Square-law MOSFET model (long-channel approximation)</li>
                        <li>Single-stage gates only</li>
                    </ul>
                </div>
            </div>

            <!-- Contributing -->
            <div class="section" id="contributing">
                <h2>🤝 Contributing</h2>
                <p style="font-size: 1.1em; margin-bottom: 20px;">We welcome contributions! Here's how you can help:</p>
                <ul style="font-size: 1.05em;">
                    <li>🔬 Adding more CMOS technologies (sub-0.18µm processes)</li>
                    <li>🎭 Implementing additional logic styles (DCVSL, PTL, Domino)</li>
                    <li>📊 Enhancing visualization features</li>
                    <li>🧮 Improving calculation accuracy with advanced models</li>
                    <li>📄 Adding export functionality (PDF, CSV, JSON)</li>
                    <li>🌐 Creating web interface</li>
                    <li>📚 Writing documentation and tutorials</li>
                </ul>
            </div>

            <!-- References -->
            <div class="section" id="references">
                <h2>📚 References</h2>
                <ul style="font-size: 1.05em;">
                    <li><strong>Weste, N. H. E., & Harris, D.</strong> (2010). <em>CMOS VLSI Design: A Circuits and Systems Perspective</em> (4th ed.). Addison-Wesley.</li>
                    <li><strong>Rabaey, J. M., Chandrakasan, A., & Nikolic, B.</strong> (2003). <em>Digital Integrated Circuits: A Design Perspective</em> (2nd ed.). Prentice Hall.</li>
                    <li><strong>Sedra, A. S., & Smith, K. C.</strong> (2015). <em>Microelectronic Circuits</em> (7th ed.). Oxford University Press.</li>
                    <li><strong>BSIM Model Documentation</strong> - Berkeley Short-channel IGFET Model</li>
                    <li><strong>MOSIS Integrated Circuit Fabrication Service</strong> - Process specifications</li>
                </ul>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <div class="footer-content">
                <h3>⭐ Star This Repository ⭐</h3>
                <p style="font-size: 1.1em; margin: 20px 0;">If you find this tool useful, please consider giving it a star!</p>
                <p style="margin: 15px 0;">
                    <a href="https://github.com/yourusername/cmos-logic-analyzer">GitHub Repository</a> • 
                    <a href="https://github.com/yourusername/cmos-logic-analyzer/issues">Report Bug</a> • 
                    <a href="https://github.com/yourusername/cmos-logic-analyzer/issues">Request Feature</a>
                </p>
                <div class="social-links">
                    <div class="social-icon" title="GitHub">🐙</div>
                    <div class="social-icon" title="LinkedIn">💼</div>
                    <div class="social-icon" title="Twitter">🐦</div>
                    <div class="social-icon" title="Email">📧</div>
                </div>
                <p style="margin-top: 30px; font-size: 0.95em; opacity: 0.8;">
                    Made with ❤️ for VLSI Engineers | © 2024 CMOS Logic Analyzer
                </p>
                <p style="margin-top: 10px; font-size: 1.1em; font-weight: 600;">
                    Happy Designing! 🚀
                </p>
            </div>
        </div>
    </div>

    <script>
        // Generate floating particles
        const particlesContainer = document.getElementById('particles');
        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 20 + 's';
            particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
            particlesContainer.appendChild(particle);
        }

        // Smooth scrolling for navigation links
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // Add animation on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.section').forEach(section => {
            observer.observe(section);
        });
    </script>
</body>
</html>
