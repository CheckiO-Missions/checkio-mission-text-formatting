//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function textFormattingCanvas(dom, data) {
            if (! data || ! data.ext) {
                return
            }

            const output = data.out

            /*----------------------------------------------*
             *
             * init
             *
             *----------------------------------------------*/
            const rows = output.split('\n')
            const width = Math.max(...rows.map(row=>row.length))
            const height = rows.length

            /*----------------------------------------------*
             *
             * write
             *
             *----------------------------------------------*/
            dom.style.fontSize = 16*(Math.min(1, 38/width))+'px'
            dom.style.fontWeight= 'bold'
            dom.style.fontFamily = 'Consolas'
            dom.style.color = '#294270'

            rows.forEach(row=>{
                const p = document.createElement('p')
                p.innerHTML = row.replace(/\s/g, '&nbsp;')
                p.style.margin = '3px'
                dom.appendChild(p)
            })
        }

        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'text_formatting',
                js: 'textFormatting'
            },
            animation: function($expl, data){
                textFormattingCanvas(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
