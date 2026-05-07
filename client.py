from __future__ import annotations

from typing import Any

from kimina_client import KiminaClient


class Lean4Client(KiminaClient):
    """Backward-compatible client used by the repository examples."""

    def __init__(
        self,
        base_url: str | None = None,
        api_url: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(api_url=api_url or base_url, **kwargs)

    def verify(
        self,
        codes: list[dict[str, Any]],
        timeout: int = 300,
        infotree_type: str | None = None,
        disable_cache: bool = False,
    ) -> Any:
        payload = {
            "codes": codes,
            "timeout": timeout,
            "infotree_type": infotree_type,
            "disable_cache": disable_cache,
        }
        return self._query(self.build_url("/verify"), payload)
