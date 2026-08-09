import allure


def setup_tracing(request, page) -> None:
    page.context.tracing.start(screenshots=True, snapshots=True)
    request.node._page = page


def finalize_tracing(request, page, context=None):
    trace_path = f"/tmp/trace-{request.node.name}.zip"
    page.context.tracing.stop(path=trace_path)
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(page.screenshot(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
        allure.attach.file(trace_path, name="trace",
                          attachment_type=allure.attachment_type.ZIP)
    if context:
        context.close()
