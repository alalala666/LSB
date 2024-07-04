import cv2
import numpy as np
import binascii

class LSB:
    '''
    這段程式碼是一個使用 LSB (Least Significant Bit) 技術進行圖片隱寫術 (Steganography) 的例子。
    隱寫術是一種在圖片中隱藏訊息的方法。
    
    本程式碼由三個主要部分組成：文本填充方法 (txt_fill)，隱藏訊息方法 (secret)，和提取隱藏訊息方法 (get_secret)。
    '''
    max_txt = 5000

    @staticmethod
    def txt_fill(txt):
        '''
        這個靜態方法將文本填充到固定長度（5000個字元）：
        '''
        # 原始字符串
        original_string = txt

        # 單個全形空格字符串
        full_width_space = "　"

        # 計算需要多少全形空格來達到 max_txt 字元
        desired_length = LSB.max_txt
        current_length = len(original_string)

        # 計算需要添加的全形空格數
        spaces_needed = desired_length - current_length

        # 創建最終字符串
        final_string = original_string + full_width_space * spaces_needed

        return final_string

    @staticmethod
    def secret(input_path, text,save_path):
        # 讀取圖片
        image = np.uint8(cv2.imread(input_path))
        # OpenCV 讀取圖片的默認顏色順序是 BGR，需要轉換為 RGB 顏色順序
        image_rgb = image
        # 記錄原始形狀
        original_shape = image_rgb.shape
        # 將圖片拉平成一維向量
        image_flattened = image_rgb.flatten()

        # 填充字符串至 max_txt 字元
        filled_text = LSB.txt_fill(text)
        utf8_encoded = filled_text.encode('utf-8')

        # 將 UTF-8 編碼轉換為二進位字符串
        binary_representation = ''.join(format(byte, '08b') for byte in utf8_encoded)
        
        for idx in range(len(binary_representation)):
            if binary_representation[idx] == '0' and image_flattened[idx] % 2 == 1:
                image_flattened[idx] -= 1
            elif binary_representation[idx] == '1' and image_flattened[idx] % 2 == 0:
                image_flattened[idx] += 1

        # 將一維向量轉回原始形狀的圖片
        image_reshaped = image_flattened.reshape(original_shape)
        image_reshaped = image_reshaped.astype(np.uint8)
        cv2.imwrite(save_path, image_reshaped)

    @staticmethod      
    def get_secret(input_path):
        # 讀取圖片
        image = np.uint8(cv2.imread(input_path))
        # OpenCV 讀取圖片的默認顏色順序是 BGR，需要轉換為 RGB 顏色順序
        image_rgb = image
        # 將圖片拉平成一維向量
        image_flattened = image_rgb.flatten()
        
        # 提取二進位字符串
        binary_string = ''.join(str(image_flattened[idx] % 2) for idx in range(LSB.max_txt * 8))
        
        # 將二進位字符串轉回 UTF-8 編碼
        n = int(binary_string, 2)
        byte_length = (n.bit_length() + 7) // 8
        utf8_encoded_again = n.to_bytes(byte_length, 'big')

        # 將 UTF-8 編碼轉回原字符串
        decoded_string = utf8_encoded_again.decode('utf-8', errors='ignore')
        return decoded_string.split('　')[0]

# lsb = LSB
# lsb.secret(input_path='uploaded_image.png', text="去NCCU Lias 403 找我 謝謝",save_path='uploaded_image2.png')
# secret_txt = lsb.get_secret(input_path='uploaded_image2.png')
# print(secret_txt)
