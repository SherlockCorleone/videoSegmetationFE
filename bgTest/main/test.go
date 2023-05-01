package main

import (
    "fmt"
    "net/http"
	"encoding/json"
)

func main() {
    http.HandleFunc("/video/upload", func(w http.ResponseWriter, r *http.Request) {
        // 设置 CORS 响应头
        w.Header().Set("Access-Control-Allow-Origin", "*")
        w.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS")
        w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

        if r.Method == "OPTIONS" {
            w.WriteHeader(http.StatusNoContent)
            return
        }
		
		fmt.Printf("Get VideoFile\n")
        fmt.Printf("%s %s %s\n", r.Method, r.URL.Path, r.Proto)
        fmt.Printf("Content-Length: %d\n", r.ContentLength)
        fmt.Printf("Content-Type: %s\n", r.Header.Get("Content-Type"))

        // 读取请求正文
        file, header, err := r.FormFile("video")
        if err != nil {
            http.Error(w, err.Error(), http.StatusBadRequest)
            return
        }
        defer file.Close()

        fmt.Printf("File Name: %s\n", header.Filename)
        fmt.Printf("File Size: %d bytes\n", header.Size)
        // 处理上传的文件内容
        // ...

        w.Write([]byte("Video uploaded successfully"))
    })
    http.HandleFunc("/sceneboundary/getboundary",func(w http.ResponseWriter, r *http.Request) {
		// 设置 CORS 响应头
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "GET, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

        response:=map[string]string{"msg":"操作成功","code":200,"sceneBoundary":{"sceneBoundaryId":7,"sceneBoundaryUrl":"F:/Work/CODE/Web/bacgroundClip/bgTest/SC20230422174818.ndjson","sceneBoundaryType":2,"shotBoundaryType":2,"videoId":4,"createDate":"2023-04-23T09:02:43.000+00:00"}}
        json.NewEncoder(w).Encode(response)
    })
	
    http.ListenAndServe(":8080", nil)
}