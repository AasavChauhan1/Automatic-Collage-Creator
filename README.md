
# Automatic Collage Creator

![Python Version](https://img.shields.io/badge/python-3.x-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌟 Overview
The **Automatic Collage Creator** is a Python-based project that simplifies the creation of 3x3 grid collages from images stored in subfolders. This tool is perfect for content creators, especially those managing Instagram carousels or similar platforms, as it eliminates the manual effort of creating preview collages.

## ✨ Features
- Automatically scans all subfolders within a parent folder.
- Creates a 3x3 grid collage of images from each subfolder.
- Saves the collages with a prefixed filename to ensure they are listed first in the folder.
- Fully customizable grid size and image dimensions.

## 📂 Folder Structure
```
Automatic-Collage-Creator/
├── README.md
├── collage_creator.py      # Python script for creating collages
├── requirements.txt        # Dependencies for the project
├── example_subfolders/     # Example folders containing images
    ├── Folder1/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   ├── ...
    └── Folder2/
        ├── image1.jpg
        ├── image2.jpg
        ├── ...
                            # Generated collages (optional location)
```

## 🛠️ Technologies Used
- **Python**: Core language for development.
- **Pillow**: Python Imaging Library (PIL) used for image processing.

## 🚀 How to Use
### Prerequisites
- Install Python 3.x on your system.
- Install the required dependencies using `pip install -r requirements.txt`.

### Setup and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/AasavChauhan1/Automatic-Collage-Creator.git
   cd Automatic-Collage-Creator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your subfolders containing images inside the main folder (e.g., `example_subfolders/`).

4. Run the script:
   ```bash
   python collage_creator.py
   ```

5. Find the generated collages saved in their respective subfolders or the specified `outputs/` directory.

### Example
If you have a folder structure like:
```
example_subfolders/
├── Nature/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── ...
├── Animals/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── ...
```
The script will generate:
```
example_subfolders/
├── Nature/
│   ├── _collage.jpg
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── ...
├── Animals/
│   ├── _collage.jpg
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── ...
```

## 📸 Sample Output
Here’s an example of a generated collage:

![Sample Collage](https://github.com/user-attachments/assets/5978e047-c315-44cb-b478-c94c99a56a96)


*Example 3x3 collage with 9 images.*

## 🔧 Customization
You can adjust these settings in the script:
- **Grid Size**: Change `grid_size=(3, 3)` to adjust the number of rows and columns.
- **Image Dimensions**: Modify `image_size=(300, 300)` to resize images as per your needs.
- **Output Filename Prefix**: Edit `output_name_prefix` to change the prefix (e.g., `_collage` or `00_collage`).

## 📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

## 🤝 Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## 🌐 Connect
For queries or suggestions, contact:
- **Name**: Aasav Chauhan
- **GitHub**: [@AasavChauhan1](https://github.com/your-username)
- **LInked In**: [@Aasav Chauhan](https://www.linkedin.com/in/aasav-chauhan/)
- **Instagram**: [@aasav_chauhan](https://instagram.com/your_handle)
---

Happy coding! 🚀
```

---

### **Steps to Use**
1. Replace placeholders (`your-username`, `your_handle`, etc.) with your real details.
2. Add a sample output image in the repository and update the `Sample Output` section with the actual image link.
3. Commit the file to your repository.  

Let me know if you need further adjustments! 🚀
