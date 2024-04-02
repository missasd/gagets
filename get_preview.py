import cv2
def get_img_from_camera_net(folder_path):
    cap = cv2.VideoCapture("rtsp://admin:xxzx80709@192.168.70.2/ch1/stream1")#获取网络摄像机
    
    i = 1
    while i<2:
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        print (str(i))
        cv2.imwrite(folder_path + str(i) + '.jpg', frame)# 存储为图像
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        i += 1
    cap.release()
    cv2.destroyAllWindows()

def get_img_from_camera_net1(folder_path):
    cap = cv2.VideoCapture("rtsp://admin:xxzx80709@192.168.70.2/ch2/stream1")#获取网络摄像机
    
    i = 1
    while i<2:
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        print (str(i))
        cv2.imwrite(folder_path + str(i) + '2.jpg', frame)# 存储为图像
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        i += 1
    cap.release()
    cv2.destroyAllWindows()
 
# 测试
if __name__ == '__main__':
    folder_path = 'D:\camera\camera'
    get_img_from_camera_net(folder_path)
    get_img_from_camera_net1(folder_path)