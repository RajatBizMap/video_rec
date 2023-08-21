frappe.ui.form.on('Material Request', {
	 refresh: function(frm) {
          frm.add_custom_button(__('Start'), function(){
                 frappe.call({ 
                  method:'video_rec.video_rec.doctype.material_request.camera_recoder',
                 args: {
                    doc:''
               }
                 
                })
             }),
             frm.add_custom_button(__('Stop'), function(){
                 frappe.call({ 
                  method:'video_rec.video_rec.doctype.material_request.compress_video',
                 args: {
                    doc:''
               }
                 
                })  
             })
	 }
});

