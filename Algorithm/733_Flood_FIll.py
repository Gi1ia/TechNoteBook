class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or not image[0]:
            return [[]]
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
            return [[]]
        
        oldColor = image[sr][sc]
        
        # Note: Have to check this, otherwise there will be a dead loop
        if oldColor == newColor:
            return image
        
        self.changeColor(image, sr, sc, oldColor, newColor)
        
        return image
        
        
    def changeColor(self, image, x, y, oldColor, newColor):
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
            return
        
        if image[x][y] != oldColor:
            return
        
        image[x][y] = newColor
        
        self.changeColor(image, x - 1, y, oldColor, newColor)
        self.changeColor(image, x, y - 1, oldColor, newColor)
        self.changeColor(image, x + 1, y, oldColor, newColor)
        self.changeColor(image, x, y + 1, oldColor, newColor)
        