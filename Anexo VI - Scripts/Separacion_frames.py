def separar_en_frames(video_path, output_folder):
    import cv2
    import os
    
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            break  

        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f" Se han extraído {frame_count} frames en {output_folder}")
    return frame_count

