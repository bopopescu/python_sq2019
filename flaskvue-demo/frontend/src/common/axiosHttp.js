import axios from 'axios'
import dcs from './dcs'
const baseURL = dcs.baseURL // localhost

axios.interceptors.response.use(function (response) {
  // 请求发送前对响应数据做点什么
  return response
}, function (error) {
  // 对响应错误做点什么
  return Promise.reject(error)
})

export default function ajax (options) {
  const ajaxObj = {
    method: options.method,
    baseURL: options.baseURL || baseURL,
    url: options.url,
    timeout: 10000,
    headers: {
      'Content-type': 'application/json;charset=UTF-8'
    },
    data: JSON.stringify({body: options.data || null})
  }
  return axios(ajaxObj)
}
