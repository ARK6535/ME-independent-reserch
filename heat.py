import numpy as np
import matplotlib.pyplot as plt
import time as time

# 変数を初期化
grid_size = 200  # 領域のサイズ
steps = 50  # シミュレーションのステップ数
diffusion_coefficient = 0.1  # 拡散係数

# グリッドを0に初期化
grid = np.zeros((grid_size, grid_size))
# grid = np.random.randint(0, 100, (grid_size, grid_size))
#グリッドの外周をランダムな温度分布にする
grid[0, :] = 100
grid[grid_size-1, :] = 100
grid[:, 0] = 100
grid[:, grid_size-1] = 100

# グリッドの中央に高温の点を設定
grid[grid_size//2-1:grid_size//2+1, grid_size//2-1:grid_size//2+1] = 100

# プロットの初期化
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='hot', interpolation='nearest')

# 温度の更新
def update(num):

    global grid

    new_grid = grid.copy()
    
    # それぞれの点で次の温度を計算
    for i in range(1, grid_size-1):
        for j in range(1, grid_size-1):
            temp = grid[i, j]
            delta = (
                grid[i+1, j] + grid[i-1, j] +
                grid[i, j+1] + grid[i, j-1] + grid[i+1, j+1] + grid[i-1, j-1] +
                grid[i-1, j+1] + grid[i+1, j-1]-
                8 * temp
            )
            new_grid[i, j] = temp + diffusion_coefficient * delta
    new_grid[0, :] = 100
    new_grid[grid_size-1, :] = 100
    new_grid[:, 0] = 100
    new_grid[:, grid_size-1] = 100
    grid = new_grid
    im.set_array(grid)
    time.sleep(0.01)

# 描画
import matplotlib.animation as animation
ani = animation.FuncAnimation(fig, update, frames=steps)

plt.colorbar(im)
plt.title("Heat Diffusion Simulation")
plt.show()