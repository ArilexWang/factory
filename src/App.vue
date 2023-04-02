
<template>
  <div>
    <el-input v-model="num1" placeholder="请输入D"></el-input>
    <el-input v-model="num2" placeholder="请输入X"></el-input>
    <el-input v-model="num3" placeholder="请输入Y"></el-input>
    <el-input v-model="num4" placeholder="请输入件数"></el-input>
    <el-button @click="calculateSum" type="primary">计算</el-button>
    <div>
      <span>单件价格: {{ sum }}</span>
    </div>
    <div>
      <span>工资: {{ salary }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { tables } from './stores/table'

const num1 = ref('')
const num2 = ref('')
const num3 = ref('')
const num4 = ref('')
const sum = ref(0)
const salary = ref(0)

const DArr = [0, 30, 31, 51, 71, 86]
const XArr = [120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540]
const YArr = [120, 150, 180, 210, 240, 270, 300, 330, 360]

const calculateSum = () => {
  const D = Number(num1.value);
  const X = Number(num2.value);
  const Y = Number(num3.value);
  const count = Number(num4.value);
  console.log('aaaaa')
  const actualD = findIndex(DArr, D)
  const actualX = findIndex(XArr, X)
  const actualY = findIndex(YArr, Y)
  console.log('实际D', actualD, '实际X', actualX, 'Y', actualY)
  console.log(tables)
  // 在tables中查找元素
  const result = tables.find(item => item.d === actualD && item.x === actualX && item.y === actualY);
  if (result) {
    console.log(result)
    sum.value = result.value;
  }
  salary.value = sum.value * count * 0.7 * 0.05
};

const findIndex = (nums: number[], num: number): number => {
  let left = 0;
  let right = nums.length - 1;
  let mid = 0;
  if (num > nums[nums.length - 1]) {
    return nums[nums.length - 1]
  }
  while (left <= right) {
    mid = Math.floor((left + right) / 2);

    if (nums[mid] === num) {
      return nums[mid];
    } else if (nums[mid] > num) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  console.log('aaa', nums[1])
  return nums[left];
}

</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
