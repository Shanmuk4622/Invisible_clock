# 🕒 Invisible Clock

The **Invisible Clock** is a real-time computer vision project that uses a webcam to create the illusion of invisibility. By detecting a black-colored object (like a cloak or card), the program replaces that region with the background, creating a seamless invisibility effect.

---

## ✨ Features

- Real-time invisibility effect using OpenCV
- Live background capture
- Color detection via HSV masking
- Adjustable HSV calibration using a dedicated utility
- Video output support (optional)
- Simple, beginner-friendly codebase

---

## 📁 Project Structure


---

## 🛠 Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

Install dependencies:

```bash
pip install opencv-python numpy
``` 
---

## 🚀 How to Use
1. [Optional] Calibrate HSV Range
To fine-tune the color detection for your cloak or object:

```bash
python findhsv.py
```
Adjust the HSV sliders until your cloak is fully detected in the "Mask" window.

Press q to quit and note the printed HSV ranges.

Update the lower_black and upper_black values in **final.py** accordingly.
---

## 2. Run the Invisible Clock
Ensure your black-colored cloak or object is ready, then:

```bash
python final.py
```
Stand in front of your camera after a few seconds of background capture.

The black-colored object will become "invisible."

**Press 'q'** to exit the program.
---
## 🧪 Example HSV Range for Black
```python
lower_black = np.array([0, 0, 0])
upper_black = np.array([96, 49, 111])
```
🔧 Tip: These ranges work well for standard black cloth. Use findhsv.py for other colors.

---


## 🎥 Record Output Video
To record the effect:

Uncomment this line in final.py:

```python
# out.write(finalOutput)
```
The video will be saved as **output.avi** in the current directory.

---
### 📌 Notes
Ensure the background remains static during the first few seconds.

Good lighting and a plain background improve results.

Best results are achieved using a cloak with a consistent dark shade.

## 📄 License
This project is licensed under the MIT License. Feel free to modify and use it for your own projects.

### 🙌 Acknowledgements
Inspired by the "Invisibility Cloak" concept made popular by the Harry Potter series and widely explored in the OpenCV community.
