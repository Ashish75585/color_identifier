import cv2
import numpy as np



class ColorIdentifier:
    def __init__(self):
        pass

    def create_bar(self, height, width, color):
        bar = np.zeros((height, width, 3), np.uint8)
        bar[:] = color
        red, green, blue = int(color[2]), int(color[1]), int(color[0])
        return bar, (red, green, blue)

    def identify_color(self, path):
        img = cv2.imread(path)
        height, width, _ = np.shape(img)
        # print(height, width)

        data = np.reshape(img, (height * width, 3))
        data = np.float32(data)

        number_clusters = 7
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        flags = cv2.KMEANS_RANDOM_CENTERS
        compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)
        # print(centers)

        font = cv2.FONT_HERSHEY_SIMPLEX
        bars = []
        rgb_values = []

        bar_height = 150
        bar_width = 150

        for index, row in enumerate(centers):
            bar, rgb = self.create_bar(bar_height, bar_width, row)
            bars.append(bar)
            rgb_values.append(rgb)

        img_bar = np.hstack(bars)

        for index, row in enumerate(rgb_values):
            image = cv2.putText(img_bar,  # image
                                f'RGB: {row}',  # text
                                (5 + bar_width * index, bar_height - 10),  # position of the text
                                font,  # font of the text
                                0.4,  # font size
                                (255, 0, 0),  # text color
                                1,  # font stroke
                                cv2.LINE_AA  #
                                )
            # print(f'{index + 1}. RGB{row}')

        # cv2.imshow('Image', img)  # use to display the image
        cv2.imshow('Dominant colors', img_bar)  # use to display the image colors.
        # cv2.imwrite('output/bar.jpg', img_bar)

        cv2.waitKey(0)