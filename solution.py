class Solution(object):
    def numOffices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0

        def mark_island(grid, x, y, visited):
            # Checks if position is within grid
            if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[x]) - 1:
                return ''

            # Checks if position has been visited
            if visited[x][y] == True:
                return ''
            visited[x][y] = True
            
            # Checks if position is 0
            if grid[x][y] == '0':
                return ''

            # Repeat the same procedure for adjacent positions at x and y
            mark_island(grid, x - 1, y, visited)
            mark_island(grid, x + 1, y, visited)
            mark_island(grid, x, y - 1, visited)
            mark_island(grid, x, y + 1, visited)
        
        # Creates an empty positions visited checker matrix
        visited = []
        for i in range(len(grid)):
            visited.append(['' for item in grid[0]])

        # Check all positions, if position hasn't been visited and is iguals '1' 
        # sum 1 to result and turn visited position True
        # All the separated groups of 1 will be counted
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if not visited[x][y] and grid[x][y] == '1':
                    result += 1
                    mark_island(grid, x, y, visited)
                visited[x][y] = True
        return result
        

        

def get_matrix():
    row = int(input())
    col = int(input())
    grid = [["0"]*col]*row

    for i in range(row):
        line = input()
        grid[i] = list(line)[0:col]
    return grid

        
if __name__ == "__main__":
    sol = Solution()
    matrix = get_matrix()
    offices = sol.numOffices(matrix)
    print(offices)