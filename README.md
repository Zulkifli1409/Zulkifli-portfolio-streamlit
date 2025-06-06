# 🌟 Personal Portfolio Website

A modern, interactive portfolio website built with Streamlit, featuring a sleek dark theme with elegant gold accents. This responsive web application showcases professional skills, projects, and experience in an engaging and user-friendly interface.

## ✨ Features

- **🎨 Modern Dark Theme**: Elegant dark design with premium gold accents
- **📱 Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **⚡ Interactive UI**: Smooth transitions, animations, and hover effects
- **🔍 Dynamic Content**: Real-time project filtering and search functionality
- **📊 Data Visualization**: Interactive charts and progress indicators
- **🎯 Performance Optimized**: Fast loading and smooth user experience

## 🏗️ Built With

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) | Core programming language |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) | Web framework |
| ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white) | Interactive visualizations |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) | Custom styling |
| ![Font Awesome](https://img.shields.io/badge/Font_Awesome-339AF0?logo=fontawesome&logoColor=white) | Icons |

## 📂 Project Structure

```
portfolio/
├── 📄 main.py              # Main application entry point
├── 🏠 home.py              # Home page component
├── 👤 about.py             # About page component  
├── 🛠️ skills.py            # Skills showcase component
├── 📂 projects.py          # Projects gallery component
├── 📞 contact.py           # Contact information component
├── 📋 requirements.txt     # Python dependencies
├── 📖 README.md            # Project documentation
└── 📁 assets/              # Static assets (images, icons)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Git (for cloning)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/zulkifli1409/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open in browser**
   - Local URL: `http://localhost:8501`
   - Network URL: Will be displayed in terminal

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit>=1.28.0
plotly>=5.15.0
requests>=2.31.0
streamlit-option-menu>=0.3.6
streamlit-lottie>=0.0.5
```

## 🎯 Page Details

### 🏠 Home Page
- **Hero Section**: Animated introduction with call-to-action
- **Featured Projects**: Showcase of top projects
- **Quick Stats**: Key metrics and achievements
- **Modern Layout**: Card-based responsive design

### 👤 About Page
- **Personal Story**: Professional background and journey
- **Services**: Offered services and expertise
- **Education**: Academic background and certifications
- **Interests**: Personal hobbies and activities

### 🛠️ Skills Page
- **Interactive Progress Bars**: Visual skill proficiency indicators
- **Radar Chart**: Comprehensive skills overview
- **Skill Categories**: Organized by technology and expertise
- **Animated Cards**: Engaging skill presentation

### 📂 Projects Page
- **GitHub Integration**: Direct connection to repositories
- **Advanced Filtering**: Filter by technology, category, or date
- **Search Functionality**: Find projects quickly
- **Project Details**: Comprehensive project information

### 📞 Contact Page
- **Multiple Contact Methods**: Email, phone, social media
- **Contact Form**: Direct message functionality
- **Social Links**: Professional social media profiles
- **FAQ Section**: Frequently asked questions

## 🎨 Customization

### Adding New Sections
1. Create a new Python file in the root directory
2. Import in `main.py`
3. Add to the navigation menu
4. Update styling as needed

### Modifying Content
- Update personal information in each component file
- Modify project data in `projects.py`
- Adjust skills and proficiency levels in `skills.py`
- Customize contact information in `contact.py`

## 🔧 Development

### Running in Development Mode
```bash
streamlit run main.py --server.runOnSave true
```

### Code Structure
- **Modular Design**: Each page is a separate component
- **Reusable Functions**: Common utilities in separate modules
- **Clean Code**: Follows PEP 8 style guidelines
- **Documentation**: Comprehensive inline comments

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Performance

- **Loading Time**: < 2 seconds on average
- **Mobile Responsive**: 100% compatibility
- **Cross-browser**: Works on all modern browsers
- **SEO Optimized**: Proper meta tags and structure

## 🐛 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
streamlit run main.py --server.port 8502
```

**Module Not Found**
```bash
pip install -r requirements.txt --upgrade
```

**Styling Issues**
- Clear browser cache
- Check CSS syntax in style tags
- Verify Streamlit version compatibility

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Zulkifli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👤 Author

**Zulkifli**
- 🌐 GitHub: [@zulkifli1409](https://github.com/zulkifli1409)
- 💼 LinkedIn: [Zulkifli](https://linkedin.com/in/zulkifli)
- 📧 Email: zul140904@gmail.com

## 🙏 Acknowledgments

- [Streamlit Team](https://streamlit.io/) for the incredible framework
- [Plotly](https://plotly.com/) for beautiful visualizations
- [Font Awesome](https://fontawesome.com/) for the icon library
- [Google Fonts](https://fonts.google.com/) for typography
- Open source community for inspiration and support

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/zulkifli1409/portfolio/issues).

### How to Contribute
1. Read the [Contributing Guidelines](CONTRIBUTING.md)
2. Fork the project
3. Create your feature branch
4. Make your changes
5. Test thoroughly
6. Submit a pull request

## ⭐ Show Your Support

Give a ⭐️ if this project helped you! Your support motivates continued development and improvement.

## 📈 Roadmap

- [ ] Add blog section
- [ ] Implement dark/light theme toggle
- [ ] Add project demo videos
- [ ] Integrate with CMS for easy content updates
- [ ] Add analytics dashboard
- [ ] Implement PWA features

## 📞 Contact & Support

For questions, suggestions, or support:

- 📧 **Email**: zul140904@gmail.com
- 💼 **LinkedIn**: [Connect with me](https://linkedin.com/in/zulkifli)
- 🐛 **Issues**: [Report bugs or request features](https://github.com/zulkifli1409/portfolio/issues)

---

<div align="center">

**Made with ❤️ by Zulkifli**

[⬆ Back to top](#-personal-portfolio-website)

</div>
