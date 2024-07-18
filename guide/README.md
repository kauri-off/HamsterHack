# Гайд как получить токен
### 1. Для начала нужно установить расшерение
 [Resource Override](https://chromewebstore.google.com/detail/resource-override/pkoacgokdfckfpndoffpifphamojphii)
![1](./1.png)

### 2. Установите такие же настройки и нажмите Edit file
![2](./2.png)

### 3. Вставьте этот код:
```js
if(location.hostname === "hamsterkombatgame.io") {
    const original_indexOf = Array.prototype.indexOf
    Array.prototype.indexOf = function (...args) {
        if(JSON.stringify(this) === JSON.stringify(["android", "android_x", "ios"])) {
            setTimeout(() => {
                Array.prototype.indexOf = original_indexOf
            })
            return 0
        }
        return original_indexOf.apply(this, args)
    }
}
```
![3](./3.png)

### 4. Теперь нажминте F12 и откройтке хомяка в браузере
![4](./4.png)

### 5. В одном из запросов найдите токен и полностью скопируйте его
![5](./5.png)

### Затем создайте папку `env` а в ней файл `.env` и вставьте в него токен
```toml
TOKEN="Bearer <То что вы скопировали>"
```