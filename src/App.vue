
<template>
  <div>
    <div class="row">
      <span style="margin-right: 5px;">D : </span>
      <el-input ref="input1" v-model="num1" placeholder="请输入D" @keydown.enter="handleEnter($event, input2, 'D')">
      </el-input>
    </div>
    <div class="row">
      <span style="margin-right: 5px;">X : </span>
      <el-input ref="input2" v-model="num2" placeholder="请输入X" @keydown.enter="handleEnter($event, input3, 'X')">
      </el-input>
    </div>
    <div class="row">
      <span style="margin-right: 5px;">Y : </span>
      <el-input ref="input3" v-model="num3" placeholder="请输入Y" @keydown.enter="handleEnter($event, input4, 'Y')">
      </el-input>
    </div>
    <div class="row">
      <span style="margin-right: 5px;">件数: </span>
      <el-input ref="input4" v-model="num4" placeholder="请输入件数" @keydown.enter="handleEnter($event, input1, 'Count')">
      </el-input>
    </div>
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
import { nextTick, ref } from 'vue';
import { tables } from './stores/table'
const input1 = ref(null);
const input2 = ref(null);
const input3 = ref(null);
const input4 = ref(null);

const handleEnter = (event: null | { preventDefault: () => void; }, input: any, key: string) => {
  event!.preventDefault();
  nextTick(() => {
    if (input && key !== 'Count') {
      input.focus();
      input.select()
    } else if (key === 'Count') {
      calculateSum()
      input.focus()
      input.select()
    }
  });
};

const num1 = ref('')
const num2 = ref('')
const num3 = ref('')
const num4 = ref('')
const sum = ref(0)
const salary = ref(0)

const DArr = [0, 30, 50, 70, 85, 100]
const XArr = [120, 150, 180, 210, 240, 270, 300, 330, 360]
const YArr = [120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570]

const calculateSum = () => {
  const D = Number(num1.value);
  const X = Number(num2.value);
  const Y = Number(num3.value);
  const count = Number(num4.value);
  const actualD = findIndex(DArr, D)
  const actualX = findIndex(XArr, X)
  const actualY = findIndex(YArr, Y)
  console.log('实际D', actualD, '实际X', actualX, 'Y', actualY)
  // 在tables中查找元素
  const result = tables.find(item => item.d === actualD && item.x === actualX && item.y === actualY);
  if (result) {
    sum.value = result.value;
    salary.value = sum.value * count * 0.7 * 0.05
    // salary.value 保留两位小数
    salary.value = Math.round(salary.value * 1000) / 1000
  } else {
    sum.value = 0
    salary.value = 0
  }
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
  return nums[left];
}

</script>

<style scoped>
.row {
  display: flex;
  flex-direction: row;
  margin: 5px;
}

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
