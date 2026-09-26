var utg = 
{
  "nodes": [
    {
      "id": "26489740492ea08d30b74dfb1ba43f76",
      "shape": "image",
      "image": ".droidbot/states/screen_2026-09-25_014400.png",
      "label": "SpaActivity\n<FIRST>",
      "package": "com.android.settings",
      "activity": ".spa.SpaActivity",
      "state_str": "26489740492ea08d30b74dfb1ba43f76",
      "structure_str": "513a00e74e97b0717682c2e85c4b1999",
      "title": "<table class=\"table\">\n<tr><th>package</th><td>com.android.settings</td></tr>\n<tr><th>activity</th><td>.spa.SpaActivity</td></tr>\n<tr><th>state_str</th><td>26489740492ea08d30b74dfb1ba43f76</td></tr>\n<tr><th>structure_str</th><td>513a00e74e97b0717682c2e85c4b1999</td></tr>\n</table>",
      "content": "com.android.settings\n.spa.SpaActivity\n26489740492ea08d30b74dfb1ba43f76\nandroid:id/content\nAllow this app to read, modify and delete all files on this device or any connected storage volumes. If granted, app may access files without your explicit knowledge.,Amaze,3.11.3,All files access,Allow access to manage all files",
      "font": "14px Arial red"
    },
    {
      "id": "b8779817c6843ac06e121dd55959391c",
      "shape": "image",
      "image": ".droidbot/states/screen_2026-09-25_014407.png",
      "label": "FileListActivity",
      "package": "me.zhanghai.android.files",
      "activity": ".filelist.FileListActivity",
      "state_str": "b8779817c6843ac06e121dd55959391c",
      "structure_str": "ee38aec3f4db040b3fe9e9d9bffd2846",
      "title": "<table class=\"table\">\n<tr><th>package</th><td>me.zhanghai.android.files</td></tr>\n<tr><th>activity</th><td>.filelist.FileListActivity</td></tr>\n<tr><th>state_str</th><td>b8779817c6843ac06e121dd55959391c</td></tr>\n<tr><th>structure_str</th><td>ee38aec3f4db040b3fe9e9d9bffd2846</td></tr>\n</table>",
      "content": "me.zhanghai.android.files\n.filelist.FileListActivity\nb8779817c6843ac06e121dd55959391c\nme.zhanghai.android.files:id/scrollView,me.zhanghai.android.files:id/buttonPanel,me.zhanghai.android.files:id/contentPanel,me.zhanghai.android.files:id/action_bar_root,me.zhanghai.android.files:id/parentPanel,android:id/button2,android:id/button1,android:id/content,me.zhanghai.android.files:id/textSpacerNoTitle,android:id/message\nCancel,App needs access to manage all files. Please allow the access in the upcoming system setting.,OK"
    },
    {
      "id": "6fb9964ba7b151c9953e45f27d1f59c2",
      "shape": "image",
      "image": ".droidbot/states/screen_2026-09-25_014421.png",
      "label": "SpaActivity\n<LAST>",
      "package": "com.android.settings",
      "activity": ".spa.SpaActivity",
      "state_str": "6fb9964ba7b151c9953e45f27d1f59c2",
      "structure_str": "513a00e74e97b0717682c2e85c4b1999",
      "title": "<table class=\"table\">\n<tr><th>package</th><td>com.android.settings</td></tr>\n<tr><th>activity</th><td>.spa.SpaActivity</td></tr>\n<tr><th>state_str</th><td>6fb9964ba7b151c9953e45f27d1f59c2</td></tr>\n<tr><th>structure_str</th><td>513a00e74e97b0717682c2e85c4b1999</td></tr>\n</table>",
      "content": "com.android.settings\n.spa.SpaActivity\n6fb9964ba7b151c9953e45f27d1f59c2\nandroid:id/content\nAllow this app to read, modify and delete all files on this device or any connected storage volumes. If granted, app may access files without your explicit knowledge.,All files access,1.7.4,Allow access to manage all files,Material Files",
      "font": "14px Arial red"
    },
    {
      "id": "9de87d11a2efe4600a9d47d4db5725ca",
      "shape": "image",
      "image": ".droidbot/states/screen_2026-09-25_014445.png",
      "label": "SpaActivity",
      "package": "com.android.settings",
      "activity": ".spa.SpaActivity",
      "state_str": "9de87d11a2efe4600a9d47d4db5725ca",
      "structure_str": "513a00e74e97b0717682c2e85c4b1999",
      "title": "<table class=\"table\">\n<tr><th>package</th><td>com.android.settings</td></tr>\n<tr><th>activity</th><td>.spa.SpaActivity</td></tr>\n<tr><th>state_str</th><td>9de87d11a2efe4600a9d47d4db5725ca</td></tr>\n<tr><th>structure_str</th><td>513a00e74e97b0717682c2e85c4b1999</td></tr>\n</table>",
      "content": "com.android.settings\n.spa.SpaActivity\n9de87d11a2efe4600a9d47d4db5725ca\nandroid:id/content\nAllow this app to read, modify and delete all files on this device or any connected storage volumes. If granted, app may access files without your explicit knowledge.,All files access,1.7.4,Allow access to manage all files,Material Files"
    }
  ],
  "edges": [
    {
      "from": "26489740492ea08d30b74dfb1ba43f76",
      "to": "b8779817c6843ac06e121dd55959391c",
      "id": "26489740492ea08d30b74dfb1ba43f76-->b8779817c6843ac06e121dd55959391c",
      "title": "<table class=\"table\">\n<tr><th>1</th><td>IntentEvent(intent='am start me.zhanghai.android.files/me.zhanghai.android.files.filelist.FileListActivity')</td></tr>\n</table>",
      "label": "1",
      "events": [
        {
          "event_str": "IntentEvent(intent='am start me.zhanghai.android.files/me.zhanghai.android.files.filelist.FileListActivity')",
          "event_id": 1,
          "event_type": "intent",
          "view_images": []
        }
      ]
    },
    {
      "from": "b8779817c6843ac06e121dd55959391c",
      "to": "6fb9964ba7b151c9953e45f27d1f59c2",
      "id": "b8779817c6843ac06e121dd55959391c-->6fb9964ba7b151c9953e45f27d1f59c2",
      "title": "<table class=\"table\">\n<tr><th>2</th><td>CustomTouchEvent(state=b8779817c6843ac06e121dd55959391c, view=90e000b992fa2cbe1fcbe7914822932e(FileListActivity/Button-OK))</td></tr>\n</table>",
      "label": "2",
      "events": [
        {
          "event_str": "CustomTouchEvent(state=b8779817c6843ac06e121dd55959391c, view=90e000b992fa2cbe1fcbe7914822932e(FileListActivity/Button-OK))",
          "event_id": 2,
          "event_type": "touch",
          "view_images": [
            "views/view_90e000b992fa2cbe1fcbe7914822932e.png"
          ]
        }
      ]
    },
    {
      "from": "6fb9964ba7b151c9953e45f27d1f59c2",
      "to": "9de87d11a2efe4600a9d47d4db5725ca",
      "id": "6fb9964ba7b151c9953e45f27d1f59c2-->9de87d11a2efe4600a9d47d4db5725ca",
      "title": "<table class=\"table\">\n<tr><th>4</th><td>CustomTouchEvent(state=6fb9964ba7b151c9953e45f27d1f59c2, view=f645993944622276fec39ccf90b3005f(SpaActivity/View-))</td></tr>\n</table>",
      "label": "4",
      "events": [
        {
          "event_str": "CustomTouchEvent(state=6fb9964ba7b151c9953e45f27d1f59c2, view=f645993944622276fec39ccf90b3005f(SpaActivity/View-))",
          "event_id": 4,
          "event_type": "touch",
          "view_images": [
            "views/view_f645993944622276fec39ccf90b3005f.png"
          ]
        }
      ]
    },
    {
      "from": "9de87d11a2efe4600a9d47d4db5725ca",
      "to": "6fb9964ba7b151c9953e45f27d1f59c2",
      "id": "9de87d11a2efe4600a9d47d4db5725ca-->6fb9964ba7b151c9953e45f27d1f59c2",
      "title": "<table class=\"table\">\n<tr><th>4</th><td>CustomTouchEvent(state=9de87d11a2efe4600a9d47d4db5725ca, view=85f6502dd64da8f20b0cfcfac384e43d(SpaActivity/View-))</td></tr>\n<tr><th>5</th><td>CustomTouchEvent(state=9de87d11a2efe4600a9d47d4db5725ca, view=e536926440a2b96e7035d03c513fb032(SpaActivity/TextView-Allow acce))</td></tr>\n</table>",
      "label": "4, 5",
      "events": [
        {
          "event_str": "CustomTouchEvent(state=9de87d11a2efe4600a9d47d4db5725ca, view=85f6502dd64da8f20b0cfcfac384e43d(SpaActivity/View-))",
          "event_id": 4,
          "event_type": "touch",
          "view_images": [
            "views/view_85f6502dd64da8f20b0cfcfac384e43d.png"
          ]
        },
        {
          "event_str": "CustomTouchEvent(state=9de87d11a2efe4600a9d47d4db5725ca, view=e536926440a2b96e7035d03c513fb032(SpaActivity/TextView-Allow acce))",
          "event_id": 5,
          "event_type": "touch",
          "view_images": [
            "views/view_e536926440a2b96e7035d03c513fb032.png"
          ]
        }
      ]
    }
  ],
  "num_nodes": 4,
  "num_edges": 4,
  "num_effective_events": 5,
  "num_reached_activities": 1,
  "test_date": "2026-09-25 01:43:31",
  "time_spent": 111.655625,
  "num_transitions": 7,
  "device_serial": "emulator-5554",
  "device_model_number": "sdk_gphone64_x86_64",
  "device_sdk_version": 35,
  "app_sha256": "22598ae8f5c4e017bd3a9313b813270056da02dbc4630d9962f30961e5c27978",
  "app_package": "me.zhanghai.android.files",
  "app_main_activity": "me.zhanghai.android.files.filelist.FileListActivity",
  "app_num_total_activities": 28
}